import pyautogui
from multiprocessing import Process
import os
import time
from PIL import Image
from pytesseract import pytesseract 

def run_bcomp():
    bcomp_path = './bcomp-ng.jar'
    os.system("java -jar " + bcomp_path)

def NZVC_check(fields_path):
    NZVC_str = ''
    try:
        pyautogui.locateOnScreen(fields_path + 'N.png')
    except:
        NZVC_str += 'N'
    
    try:
        pyautogui.locateOnScreen(fields_path + 'Z.png')
    except:
        NZVC_str += 'Z'
    
    try:
        pyautogui.locateOnScreen(fields_path + 'V.png')
    except:
        NZVC_str += 'V'
        
    try:
        pyautogui.locateOnScreen(fields_path + 'C.png')
    except:
        NZVC_str += 'C'
    
    return NZVC_str

def get_val(key: str) -> str:
    global fields
    global path_to_tesseract

    img = pyautogui.screenshot(region=(fields[key]['left'],fields[key]['top'],fields[key]['width'],fields[key]['height']))

    pytesseract.tesseract_cmd = path_to_tesseract

    text = str(pytesseract.image_to_string(img))
    
    text = text.replace(" ", "")
    text = text.replace("\n", "")

    print("Got value: ", text, "of", key, "field")
    return text

def hex_to_two(hex_str: str) -> str:
    hex_dict = dict()
    hex_dict['0'] = '0000'
    hex_dict['1'] = '0001'
    hex_dict['2'] = '0010'
    hex_dict['3'] = '0011'
    hex_dict['4'] = '0100'
    hex_dict['5'] = '0101'
    hex_dict['6'] = '0110'
    hex_dict['7'] = '0111'
    hex_dict['8'] = '1000'
    hex_dict['9'] = '1001'
    hex_dict['A'] = '1010'
    hex_dict['B'] = '1011'
    hex_dict['C'] = '1100'
    hex_dict['D'] = '1101'
    hex_dict['E'] = '1110'
    hex_dict['F'] = '1111'

    while(len(hex_str) % 4 != 0):
        hex_str = '0' + hex_str

    two_str = ""

    for item in hex_str:
        two_str += hex_dict[item]

    return two_str

def two_to_hex(two_str: str) -> str:
    two_dict = dict()
    two_dict['0000'] = '0'
    two_dict['0001'] = '1'
    two_dict['0010'] = '2'
    two_dict['0011'] = '3'
    two_dict['0100'] = '4'
    two_dict['0101'] = '5'
    two_dict['0110'] = '6'
    two_dict['0111'] = '7'
    two_dict['1000'] = '8'
    two_dict['1001'] = '9'
    two_dict['1010'] = 'A'
    two_dict['1011'] = 'B'
    two_dict['1100'] = 'C'
    two_dict['1101'] = 'D'
    two_dict['1110'] = 'E'
    two_dict['1111'] = 'F'

    while(len(two_str) % 4 != 0):
        two_str = '0' + two_str

    hex_str = ""

    while(len(two_str) > 4):
        hex_str += two_dict[two_str[:4]]
        two_str = two_str[4:]
    hex_str += two_dict[two_str[:4]]

    return hex_str

def get_input_arr(input_path):
    input_file = open(input_path, "rt+")
    input_data = list()
    
    input_file.readline()
    input_file.readline()
    line = input_file.readline()
    while(line != ''):
        data_pair = []
        line = line[2:]
        line = line[:-3]
        data_pair.append(line[:line.find(' | ')])
        data_pair.append(line[(line.find(' | ') + 3):])

        input_data.append(data_pair)

        line = input_file.readline()

    input_file.close()

    return input_data

def main(process):
    time.sleep(3)

    # Configs here
    fields_path = './fields/'
    input_path = './input.md'
    output_path = './output.md'
    global path_to_tesseract
    path_to_tesseract = r"C:\Users\Spitf\Desktop\tesseract\tesseract.exe"

    starting_position = "03E9"

    # Initializing fields
    global fields
    fields = dict()

    fields['AC'] = pyautogui.locateOnScreen(fields_path + 'AC.png')._asdict()
    fields['AC']['width'] -= fields['AC']['height']
    fields['AR'] = pyautogui.locateOnScreen(fields_path + 'AR.png')._asdict()
    fields['AR']['left'] += fields['AR']['height']
    fields['AR']['width'] -= fields['AR']['height']
    fields['BR'] = pyautogui.locateOnScreen(fields_path + 'BR.png')._asdict()
    fields['BR']['width'] -= fields['BR']['height']
    fields['C'] = pyautogui.locateOnScreen(fields_path + 'C.png')._asdict()
    fields['CR'] = pyautogui.locateOnScreen(fields_path + 'CR.png')._asdict()
    fields['CR']['left'] += fields['CR']['height']
    fields['CR']['width'] -= fields['CR']['height']
    fields['DR'] = pyautogui.locateOnScreen(fields_path + 'DR.png')._asdict()
    fields['DR']['left'] += fields['DR']['height']
    fields['DR']['width'] -= fields['DR']['height']
    fields['Interrupt'] = pyautogui.locateOnScreen(fields_path + 'Interrupt.png')._asdict()
    fields['IP'] = pyautogui.locateOnScreen(fields_path + 'IP.png')._asdict()
    fields['IP']['left'] += fields['IP']['height']
    fields['IP']['width'] -= fields['IP']['height']
    fields['IR'] = pyautogui.locateOnScreen(fields_path + 'IR.png')._asdict()
    fields['IR']['width'] -= fields['IR']['height']
    fields['N'] = pyautogui.locateOnScreen(fields_path + 'N.png')._asdict()
    fields['PS'] = pyautogui.locateOnScreen(fields_path + 'PS.png')._asdict()
    fields['PS']['width'] -= fields['PS']['height']
    fields['RAM IP'] = pyautogui.locateOnScreen(fields_path + 'RAM IP.png')._asdict()   
    fields['RAM VAL'] = pyautogui.locateOnScreen(fields_path + 'RAM VAL.png')._asdict()
    fields['SP'] = pyautogui.locateOnScreen(fields_path + 'SP.png')._asdict()
    fields['SP']['left'] += fields['SP']['height']
    fields['SP']['width'] -= fields['SP']['height']
    fields['V'] = pyautogui.locateOnScreen(fields_path + 'V.png')._asdict()
    fields['Z'] = pyautogui.locateOnScreen(fields_path + 'Z.png')._asdict()

    print("=====================")
    print("Integrated fields:")
    print("=====================")
    for key in fields.keys():
        print(key, fields[key]['left'], fields[key]['top'], fields[key]['width'], fields[key]['height'])
    print("=====================")

    # Getting input data
    input_data = get_input_arr(input_path)

    print('Starting to set data...')

    # Setting data in bcomp
    for pair in input_data:
        pyautogui.write(hex_to_two(pair[0]))
        pyautogui.press('f4')
        pyautogui.write(hex_to_two(pair[1]))
        pyautogui.press('f5')

    # Setting other bcomp settings
    pyautogui.hotkey('shift','f9')

    # Creating a pause to make user interract
    print("Setted bcomp and data. Enter smth to continue > ")
    os.system("pause")
    time.sleep(5)
    
    # returning to the first executable step
    pyautogui.write(hex_to_two(starting_position)) ## input_data[0][0]
    pyautogui.press('f4')

    # Creating output file
    output_file = open(output_path, "wt+", encoding="utf-8")
    output_file.write("<table><thead><tr><th colspan=2>Выполняемая команда</th>\
<th colspan=8>Содержимое регистров процессора после выполнения команды</th>\
<th colspan=2>Ячейка, содержимое которой изменилось после выполнения команды</th>\
</tr></thead><tbody>")
    output_file.write('<tr><td align="center">Адрес</td><td align="center">Код</td><td align="center">IP</td>\
<td align="center">CR</td><td align="center">AR</td><td align="center">DR</td>\
<td align="center">SP</td><td align="center">BR</td><td align="center">AC</td>\
<td align="center">NZVC</td><td align="center">Адрес</td><td align="center">Новый код</td></tr>')

    # Creating manual break point
    break_point = 'FFF'
    for pair in input_data:
        if pair[1] == '0100':
            break_point = pair[0]

    print("Calculated break point: ", break_point)
    
    val_IP = starting_position ## memorising variable
    val_AC = ""
    val_NZVC = ""

    # Creating loop to trace programm
    while(1):
        print("checking for break point", hex_to_two(break_point))
        print(">> Step", two_to_hex(get_val('IP')), "out of", break_point)
        if two_to_hex(get_val('IP')) == break_point:
            print("break point reached")
            break

        while(1): ## Skipping trace steps until final
            pyautogui.press('f8')
            if pyautogui.pixelMatchesColor(fields['Interrupt']['left'] + 8, fields['Interrupt']['top'] + 8, (255, 0, 0)):
                break
        
        pyautogui.press('f8')

        adress = val_IP
        
        val_IP = two_to_hex(get_val('IP'))
        val_CR = two_to_hex(get_val('CR'))
        
        code = val_CR
        
        val_AR = two_to_hex(get_val('AR'))
        val_DR = two_to_hex(get_val('DR'))
        val_SP = two_to_hex(get_val('SP'))
        val_BR = two_to_hex(get_val('BR'))
        val_AC = two_to_hex(get_val('AC'))
        val_NZVC = NZVC_check(fields_path)
        
        adress_changed = ""
        value_changed = ""

        if code[0] in ["8", "B", "E"]:
            adress_changed = val_AR
            value_changed = val_DR

        output_file.write(f'<tr><td align="center">{adress}</td><td align="center">{code}</td>\
<td align="center">{val_IP}</td><td align="center">{val_CR}</td><td align="center">{val_AR}</td>\
<td align="center">{val_DR}</td><td align="center">{val_SP}</td><td align="center">{val_BR}</td>\
<td align="center">{val_AC}</td><td align="center">{val_NZVC}</td><td align="center">{adress_changed}</td>\
<td align="center">{value_changed}</td></tr>')

    output_file.write(f'<tr><td align="center">{val_IP}</td><td align="center">0100</td>\
<td align="center">???</td><td align="center">0100</td><td align="center">{val_IP}</td>\
<td align="center">0100</td><td align="center">000</td><td align="center">{val_IP}</td>\
<td align="center">{val_AC}</td><td align="center">{val_NZVC}</td><td align="center"></td>\
<td align="center"></td></tr>')
    
    # Closing files
    output_file.write("</tbody></table>")
    output_file.close()
    
    process.terminate()


if __name__ == '__main__':
    proc1 = Process(target=run_bcomp)
    proc1.start()
    
    proc2 = Process(target=main(proc1))
    proc2.start()

    proc1.join()
    proc2.join()
    