import sys
import os
import exifread
import platform
import subprocess


def get_timestamp_from_sips(picture_file_path):
    sips_output = subprocess.run(
        ["sips", "-g", "creation", picture_file_path],
        capture_output=True,
        text=True,
    ).stdout
    sips_output_row_list = sips_output.split("\n")
    sips_output_2nd_row = sips_output_row_list[1]
    timestamp = sips_output_2nd_row.strip().strip("creation:").strip()
    return timestamp


def get_timestamp_from_exifread(picture_file):
    tags = exifread.process_file(picture_file)
    if "EXIF DateTimeOriginal" in tags:
        return tags["EXIF DateTimeOriginal"].values
    else:
        return ""


def main():
    args = sys.argv
    work_path = args[1]

    picture_file_name_list = os.listdir(work_path)

    for index, picture_file_name in enumerate(picture_file_name_list):
        picture_file_path = os.path.join(work_path, picture_file_name)

        try:
            picture_file = open(picture_file_path, "rb")
        except:
            print(
                "rename picture file [{0}/{1}] : Cannot open {2}.".format(
                    index + 1, len(picture_file_name_list), picture_file_name
                )
            )
            continue

        if platform.system() == "Darwin":
            timestamp = get_timestamp_from_sips(picture_file_path)
        else:
            timestamp = get_timestamp_from_exifread(picture_file)

        if not timestamp:
            print(
                "rename picture file [{0}/{1}] : {2} does not have timestamp.".format(
                    index + 1, len(picture_file_name_list), picture_file_name
                )
            )
            continue

        # get original file name without suffix
        picture_file_name_body = "".join((picture_file_name.split("."))[:-1])

        suffix = (picture_file_name.split("."))[-1]

        # new file name will be {timestamp}_{original file name without suffix}.{suffix}
        # example: 7M400001.ARW -> 2023-02-23_12-53-12_7M400001.ARW
        new_picture_file_name = (
            timestamp.replace(":", "-").replace(" ", "_")
            + "_"
            + picture_file_name_body
            + "."
            + suffix
        )

        print(
            "rename picture file [{0}/{1}] : {2} -> {3}".format(
                index + 1,
                len(picture_file_name_list),
                picture_file_name,
                new_picture_file_name,
            )
        )

        # close file before rename
        picture_file.close()

        os.rename(
            picture_file_path,
            os.path.join(work_path, new_picture_file_name),
        )


if __name__ == "__main__":
    main()
