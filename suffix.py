vitri = -1  
checkx = -1  
with open("./md5_data1", 'rb') as f1, open("./md5_data2", 'rb') as f2:
    data1 = f1.read()
    data2 = f2.read()
    for i in range(len(data1)):
        if data1[i] != data2[i]:
            vitri = i
            check = hex(data1[i])
            #print(vitri,check)
            break 
b = f"""<?php
$file_path = __FILE__;
$file = fopen($file_path, 'rb');
fseek($file, {vitri});
$byte = fread($file, 1);
if (ord($byte) === {check}) {{
    system('clear');
    echo "Hello everyone\nMy name is Son";
}} else {{
    system('clear');
    system('/bin/sh');
}}
fclose($file);
?>"""
print(b)
