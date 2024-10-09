# Extraction-of-IOCs-using-Regular-Expression-in-Python

In this project, we analyzed a suspicious executable file to identify potential threats and indicators of compromise (IOCs). The analysis began by scanning the sample.exe file using VirusTotal, which provided insights into known malware signatures and flagged potential risks. Next, we used Regex101, an online tool, to test regular expressions and extract IOCs such as IP addresses, URLs, and MD5 hashes from sample log data. This allowed us to detect patterns related to the malware's activities.


We then implemented a similar process in Python on Google Colab, where we defined regex patterns and applied them to log data for programmatic IOC extraction. This step enabled us to systematically identify suspicious IPs, URLs, file hashes, and registry keys from the logs.


The findings emphasized the effectiveness of using multiple tools in tandem for malware analysis and IOC detection. Countermeasures, such as blocking malicious IP addresses, flagging dangerous URLs, and removing associated registry keys, can help mitigate potential threats discovered during the analysis.
