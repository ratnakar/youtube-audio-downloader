import os

from argparse import ArgumentParser

ALLOWED_FILE_EXTENSIONS = ("txt", "csv")


def get_file_extension(path_file):
        return path_file.split(".")[-1]


def validate_file(parser, file_path):
    if not os.path.exists(file_path):
        return parser.error("The file %s does not exists" % file_path)

    file_extension = get_file_extension(file_path)

    if file_extension not in ALLOWED_FILE_EXTENSIONS:
        return parser.error("Only allow .txt and .csv files.")

    return file_path

def get_arguments():
    parser = ArgumentParser(description="Youtube Audio Downloader")
    parser.add_argument(
        "-f", metavar='FILE', type=lambda path: validate_file(parser, path),
        dest="path_file", required=True,
        help="Path to file that contains the youtube links")
    parser.add_argument(
        "-p", metavar='PATH TO SAVE', type=str, dest="path_to_save",
        default=".", help="Path to save the audios.")
    # parser.add_argument(
    #     "-o", metavar='OVERRIDE', type=str, dest="override_songs",
    #     default="yes", help="Override the existing songs?")
    args = parser.parse_args()

    return args
