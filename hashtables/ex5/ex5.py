# Your code here



def finder(files, queries):
    """
    Given a list of file paths files
    return file paths containing files in 
    list queries
    """
    paths_to_files = {}
    result = []
    for i in files:
        split_text = i.rpartition('/')
        key = split_text[0]+split_text[1]
        value = split_text[2]
        if key not in paths_to_files:
            paths_to_files[key] = [value]
        else:
            paths_to_files[key].append(value)
    
    for i in queries:
        for j in paths_to_files.keys():
            if i in paths_to_files[j]:
                if paths_to_files[j][0] == i:
                    result.append(j + paths_to_files[j][0])
                elif paths_to_files[j][1] == i:
                    result.append(j + paths_to_files[j][1])
            
                

    return result


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
