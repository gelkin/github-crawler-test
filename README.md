# github-crawler-test

The program which crawls Github. Only analyses the first page of the search.

## Input parameters

You can specify **keywords** you want to find. 
List of **proxies** you want to use, every time proxy will be chosen randomly from the list. 
There are also three **types** of search which are supported: **Repositories**, **Issues**, and **Wikis**.

## Output

URLS for each of the results of the search.

## Format

Specify the parameters you want as JSON in the **in.txt** file. The result URLS will be written to the file **out.txt** also in JSON format.

## Example

This search in the file **in.txt**:
```json
{
  "keywords": [
    "openstack",
    "nova",
    "css"
  ],
  "proxies": [
    "8.129.215.20:8080",
    "208.80.28.208:8080"
  ],
  "type": "Repositories"
}
```

If you run
```console
foo@bar:~$ python github_crawler.py
```


Will give this result in **out.txt**:
```json
[
  {
    "url": "https://github.com/atuldjadhav/DropBox-Cloud-Storage"
  },
  {
   "url": "https://github.com/michealbalogun/Horizon-dashboard"
  }
]
```




