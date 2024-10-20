<h1>migraena.py</h1>
In our main function, we first assign the directory of the copied malware to the variable copied_path and add this path to the startup. Then, we call our other functions and after inputting the files to be downloaded and their URLs, we start an infinite loop. This loop downloads the selected file to the desktop every second. As long as the user (victim) doesn’t close this .exe from the task manager, the files will continue to download. And of course, unless removed from the system startup registry, our malware will run again every time the machine starts.
<h1>step by step, how to do it</h1>
You can check my "https://alirfandogan.com/2024/07/02/migraena-malware/" where I explain the step-by-step writing process, what each library does, and the answer to the question 'why this code?'
<h1>what happens if it is (compiled and) executed?</h1>


https://github.com/user-attachments/assets/b5073b7d-d1c3-43b9-a2ac-d1d5034b588e

<h1>note</h1>
There is no example of ransomware here. It does not encrypt files, it deletes them. This malware pretends to be ransomware. Deleted files cannot be recovered. However, if the user (victim) acts on their naive feelings and sends $300 to the provided BTC address (such an address does not exist), they will receive nothing in return. As a result, this malware is designed solely to harm the person who runs the .exe file, as it does not establish any connection with the attacker’s machine. The attacker cannot steal data or navigate within the system.
