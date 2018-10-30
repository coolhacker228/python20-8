import os
import tempfile


class File():

    _add_file_name = 1

    def __init__(self, file_path):

        if not os.path.exists(file_path):
            self.f = open(file_path, 'w+')
            self.f.close()

        self.file_path = file_path


    def __str__(self):
        return (self.file_path)


    def __add__(self, obj):

        new_file_path = os.path.join(tempfile.gettempdir(), str(File._add_file_name) + '.data')
        new_file = File(new_file_path)
        
        new_file.write(self.read() + obj.read())
                    
        File._add_file_name += 1

        return (new_file)     


    def __iter__(self):
        ##with open (self.file_path, 'r') as f:
        return (self)


    def __next__(self):
        with open (self.file_path, 'r') as f:
            line = f.readline()
            if line:
                return (line)
            else:
                raise StopIteration
        
        
    
    def write(self, string_to_write):
        with open (self.file_path, 'a') as f:
            f.write(string_to_write)

    def read(self):
        with open (self.file_path, 'r') as f:
            return(f.read())


    
test = File('test.py')
##print(test.read())
for line in test:
    print(line)


    

        