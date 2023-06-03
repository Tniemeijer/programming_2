from Bio import Entrez
import pandas as pd
import ssl
import multiprocessing as mp
import time
import yaml

with open('config.yaml', 'r') as conf_file:
    config = yaml.load(conf_file,Loader=yaml.SafeLoader)

ssl._create_default_https_context = ssl._create_unverified_context

Entrez.email = config["e_mail"]

file = Entrez.elink(dbfrom="pubmed",
                   db="pmc",
                   LinkName="pubmed_pmc_refs",
                   id="30049270",
                   api_key=config["api_key"] )
results = Entrez.read(file)
references = [f'{link["Id"]}' for link in results[0]["LinkSetDb"][0]["Link"]]

def get_references_xmls(ref):
    handle =  Entrez.efetch(db="pubmed",
                        id=str(ref),
                        retmode="xml",
                        api_key=config["api_key"])
    with open(f'DATA/{ref}.xml', 'wb') as w_file:
        w_file.write(handle.read())

def get_references_xmls_multi(references):
    with mp.Pool() as p:
        p.map(get_references_xmls,references[:10])

start = time.time()
get_references_xmls_multi(references)
print(f'{time.time()-start}')