

def clean_footer(file_path, target_dir):
    file_name = file_path.split('/')[-1]
    with open(file_path, 'r') as file:
        f = file.read().splitlines()
    with open(f'{target_dir}/{file_name}', 'w') as file:
        for i in f:
            if i == '':
                break
            file.write(f'{i}\n')


def main():
    import glob
    import argparse

    parser = argparse.ArgumentParser(description='Cleaning footer of files')
    parser.add_argument('files_path_mask', metavar='files_path_mask',
                        type=str, help='Enter your files path mask.')
    parser.add_argument('target_dir', metavar='target_dir',
                        type=str, help='Enter your target directory to be stored')
    args = parser.parse_args()

    files_path_mask = args.files_path_mask
    target_dir = args.target_dir

    print(files_path_mask)

    for i in glob.glob(files_path_mask):
        print(f'Processing {i}')
        clean_footer(i, target_dir)

    print('\nCleaning Footer process is done')


if __name__ == '__main__':
    main()
