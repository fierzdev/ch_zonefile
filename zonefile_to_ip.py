#from dataclasses import dataclass
import socket

#@dataclass
#class ZonefileEntry:
#	domain: str
#	name_server: str

#zonefile = []

def process_zonefile(filename):
    out_filename = filename.split('/')[-1]
    out_file = open(f'ips/{out_filename}', 'w+')
    with open(filename) as f:
        for line in f:
            if "ns" in line:
                splitted = list(filter(None,line.strip().split("\t")))
                domain = splitted[0]
                name_server = splitted[-1]
                #zonefile.append(ZonefileEntry(splitted[0], splitted[-1]))
                try:
                    ip = socket.gethostbyname(domain)
                except socket.gaierror as e:
                    ip = None
                _ = out_file.write(f'{domain};{ip};{name_server}\n')
    out_file.close()

if __name__=='__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("filename", type=str)
    args = parser.parse_args()
    process_zonefile(args.filename)
