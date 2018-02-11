import os


# Each website you crawl is a separate project (folder)
def create_project_dir(directory):
    if not os.path.exists(directory):
        print('Creating project: {}'.format(directory))
        os.makedirs(directory)


# Create queue and crawled files (if not created)
def create_data_files(project_name, base_url):
    queue = '{}/queue.txt'.format(project_name)
    crawled = '{}/crawled.txt'.format(project_name)
    if not os.path.isfile(queue):
        write_file(queue, base_url)
    if not os.path.isfile(crawled):
        write_file(crawled, '')


# Create a new file
def write_file(path, data):
    with open(path, 'w') as f:
        f.write(data)


# add data onto an existing file
def append_to_file(path, data):
    with open(path, 'a') as f:
        f.write(data + '\n')


# Delete the contents of a file
def delete_file_contents(path):
    with open(path, 'w'):
        pass


# Read a file and convert each line to set items
def file_to_set(file_name):
    results = set()
    with open(file_name, 'rt') as f:
        for line in f:
            results.add(line.strip())
    return results


# Iterate throug a set, each item will be a new line in the line
def set_to_file(links, file):
    delete_file_contents(file)
    for link in sorted(links):
        append_to_file(file, link)


if __name__ == '__main__':
    create_project_dir('thenewboston')
    create_data_files('thenewboston', 'https://thenewboston.com/')
