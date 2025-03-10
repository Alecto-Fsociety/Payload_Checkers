import socket,ssl,sys,argparse,re,traceback,chardet,random,pathlib,itertools as it
from urllib.parse import quote,urlparse
from datetime import datetime
from multiprocessing import Pool

banner = """
▗▄▄▖  ▗▄▖▗▖  ▗▖▗▖    ▗▄▖  ▗▄▖ ▗▄▄▄      ▗▄▄▖▗▖ ▗▖▗▄▄▄▖ ▗▄▄▖▗▖ ▗▖▗▄▄▄▖▗▄▄▖  ▗▄▄▖
▐▌ ▐▌▐▌ ▐▌▝▚▞▘ ▐▌   ▐▌ ▐▌▐▌ ▐▌▐▌  █    ▐▌   ▐▌ ▐▌▐▌   ▐▌   ▐▌▗▞▘▐▌   ▐▌ ▐▌▐▌
▐▛▀▘ ▐▛▀▜▌ ▐▌  ▐▌   ▐▌ ▐▌▐▛▀▜▌▐▌  █    ▐▌   ▐▛▀▜▌▐▛▀▀▘▐▌   ▐▛▚▖ ▐▛▀▀▘▐▛▀▚▖ ▝▀▚▖
▐▌   ▐▌ ▐▌ ▐▌  ▐▙▄▄▖▝▚▄▞▘▐▌ ▐▌▐▙▄▄▀    ▝▚▄▄▖▐▌ ▐▌▐▙▄▄▖▝▚▄▄▖▐▌ ▐▌▐▙▄▄▖▐▌ ▐▌▗▄▄▞▘

by Alecto_Fsociety (https://github.com/Alecto-Fsociety)
"""
print(banner)


class Payloads:
    def __init__(self,target_url,payload_list,method,port):
        self.base = urlparse(target_url)
        self.scheme = self.base.scheme
        self.domain = self.base.netloc
        self.path = self.base.path

        self.payload_path = payload_list

        self.ua_path = "ua.txt"
        self.ua_list = self.ua_lists()
        self.dir_name = "log_payloads"
        self.err_dir_name = "log_err"
        self.date = datetime.now() 
        self.file_name = f"{self.date.year}_{self.date.month}-{self.date.day}_{self.date.hour}-{self.date.minute}_payloads.log"
        self.err_log_file_name = "err.log"

        self.cycle = it.cycle(r"/-\|")

        self.method = method.lower()
        self.port = port if port is not None else (443 if self.scheme == "https" else 80)

        self.json_data = []

    def payload_lists(self):
        return [payload.strip("\n") for payload in open(self.payload_path,"r",encoding="utf-8",errors="ignore").readlines()]

    def ua_lists(self):
        return [ua.strip("\n") for ua in open(self.ua_path,"r",encoding="utf-8").readlines()]

    def get_headers(self,payload):
        return f"GET /{self.path}?payl0ad={quote(payload)} HTTP/1.1\r\nHost:{self.domain}\r\nUser-Agent:{random.choice(self.ua_list)}\r\nAccept:*/*\r\n\r\n"

    def post_headers(self,payload):
        pay_loads = f"payl0ad={quote(payload)}"
        return f"POST /{self.path} HTTP/1.1\r\nHost:{self.domain}\r\nContent-Type:application/x-www-form-urlencoded\r\nContent-Length:{len(pay_loads)}\r\nUser-Agent:{random.choice(self.ua_list)}\r\nAccept:*/*\r\n\r\n{pay_loads}\r\n"

    def parse_headers(self,response_data):
        headers = {}
        status_match = re.search(r"HTTP/\d\.\d (\d+)", response_data)
        status = status_match.group(1) if status_match else "000"
        headers["status"] = status
        for line in response_data.split("\r\n"):
            match = re.match(r"([^:]+): (.+)", line)
            if match:
                key, value = match.groups()
                headers[key] = value
        return headers

    def requests(self):
        list_payload = self.payload_lists();lines = len(list_payload)
        pathlib.Path(self.dir_name).mkdir(exist_ok=True)
        pathlib.Path(self.err_dir_name).mkdir(exist_ok=True)

        for point,payload in enumerate(list_payload,start=1):
            err_log = f"{self.date.year}_{self.date.month}-{self.date.day}_{self.date.hour}-{self.date.minute}_err"
            try:

                sys.stdout.write(f"\r[*] Check_Payloads {self.domain}:{self.port} <{point}/{lines}> ~ {next(self.cycle)}")
                sys.stdout.flush()

                if self.scheme == "https":
                
                    with (ssl.create_default_context()).wrap_socket(
                        socket.create_connection((self.domain,self.port)),server_hostname=self.domain
                        )as ssock:
                        ssock.settimeout(3)

                        if self.method == "post":
                            ssock.send(bytes(self.post_headers(payload),"utf-8"))
                        else:
                            ssock.send(bytes(self.get_headers(payload),"utf-8"))

                        response = ssock.recv(1024*10)
                        detected = chardet.detect(response)
                        encoding = detected["encoding"] if detected["encoding"] else "utf-8"
                        response_data = response.decode(encoding, errors="ignore") 

                        json_data = self.parse_headers(response_data)

                        if json_data["status"] in {"200","301","302"}:
                            with open(f"{self.dir_name}/{self.file_name}","a+",encoding="utf-8")as files:
                                files.write(f"[+] {payload}\r\n{json_data}\r\n")
                else:
                    with socket.socket(socket.AF_INET,socket.SOCK_STREAM)as sock:
                        sock.settimeout(3)
                        sock.connect((self.domain,self.port))

                        if self.method == "post": 
                            sock.sendall(bytes(self.post_headers(payload),"utf-8"))
                        else:
                            sock.sendall(bytes(self.get_headers(payload),"utf-8"))
                        response = sock.recv(1024*10)
                        detected = chardet.detect(response)
                        encoding = detected["encoding"] if detected["encoding"] else "utf-8"
                        response_data = response.decode(encoding, errors="ignore")

                        json_data = self.parse_headers(response_data)

                        if json_data["status"] in {"200","301","302"}:
                            with open(f"{self.dir_name}/{self.file_name}","a+",encoding="utf-8")as files:
                                files.write(f"[+] {payload}\r\n{json_data}\r\n")

            except Exception as e:
                with open(f"{self.err_dir_name}/{self.err_log_file_name}","a+",encoding="utf-8")as err_files:
                    err_files.write(f"[-] {err_log} | {traceback.format_exc()}\n")

def worker(payload_instance):
    payload_instance.requests() 

def main():
    try:
        arg = argparse.ArgumentParser()

        arg.add_argument("-url",type=str,required=True,help="[>] Target_URL / -url <target_url>")
        arg.add_argument("-t",type=int,default=4,help="[>] Pool_Thread_Numbers / -t <pool_thread_numbers>")
        arg.add_argument("-m",type=str,default="GET",help="[>] Method [POST/GET] / -m <post/get>")
        arg.add_argument("-p",type=int,default=None,help="[>] Custom_Port_Number / -p <custom_port_number>")
        arg.add_argument("-w",type=str,required=True,help="[>] Payload_WordList_Path / -w <payload_wordlist_path>")
        parse = arg.parse_args()

        payload_instance = Payloads(parse.url,parse.w,parse.m,parse.p)
        with Pool(parse.t) as pool:
            pool.starmap(worker, [(payload_instance,)] * parse.t,chunksize=1)  
    except KeyboardInterrupt:
        sys.stdout.write("\n[#] Stop_Send_Payloads...\n")

if __name__ == "__main__":
    sys.exit(main())


