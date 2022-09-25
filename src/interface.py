import PySimpleGUI as sg
from pyperclip import copy, paste
from time import sleep
from cript_data import encrypt_pass, decrypt_pass

icone = r'C:\Users\Guilherme\Desktop\DESENVOLVIMENTO\PYTHON\criptPass\imgs\padlock.ico'

sg.theme('DarkGrey14')
def menuApp():
    layout = [
        [sg.Text('Selecione uma das opções:'), sg.Combo(['Encrypted', 'Decrypted'],key='-OptionMenu-', size=(15,1))],
        [sg.Button('Submit'), sg.Exit()]
            ]

    return sg.Window("CriptPass", layout=layout, icon=icone, finalize=True)

def EncryptedApp():
    
    layout = [
    [sg.Text('Entre com a senha:  '), sg.InputText(key='-PasswordText-',size=(20,1))],
    [sg.Text('Senha Criptografada:')],
    [sg.Multiline(key='-PasswordEncrypt-',size=(30, 5), disabled=True)],
    [ sg.Button('Encrypted'),sg.Button('Copy'), sg.Button('Back'), sg.Exit(), ]
        ]

    return sg.Window("CriptPass", layout=layout, icon=icone, finalize=True)


def DecryptedApp():

    
    layout = [
    [sg.Text('Entre com a senha:       '), sg.InputText(key='-PasswordEncryptFunc-',size=(20,1))],
    [sg.Text('Senha Descriptografada:')], 
    [sg.Multiline(key='-PasswordDecrypt-',size=(30,5), disabled=True)],
    [ sg.Button('Decrypted'),sg.Button('Paste'), sg.Button('Back'), sg.Exit()]
        ]

    return sg.Window("CriptPass", layout=layout, icon=icone, finalize=True)

window_menu, window_encrypt, window_decrypt = menuApp(), None, None 
while True:
    window, event, values = sg.read_all_windows()

    if window == window_menu and event in (sg.WIN_CLOSED, 'Exit'):
        break
    
    if window == window_encrypt and event in (sg.WIN_CLOSED, 'Exit'):
        break
    
    if window == window_decrypt and event in (sg.WIN_CLOSED, 'Exit'):
        break
    
    if window == window_encrypt and event == 'Back':
        window_menu['-OptionMenu-'].update('')
        window_menu.un_hide()
        window_encrypt.hide()
        
    if window == window_decrypt and event == 'Back':
        window_menu['-OptionMenu-'].update('')
        window_menu.un_hide()
        window_decrypt.hide()
    
    if window == window_menu and event == 'Submit':
        
        if values['-OptionMenu-'] == 'Encrypted':
            window_encrypt = EncryptedApp()
            
            window_menu.hide()
            
        elif values['-OptionMenu-'] == 'Decrypted':
            window_decrypt = DecryptedApp()
            window_menu.hide()
            
        else:
            sg.popup('Por favor, Escolha uma opção', title='Aviso')
            
    if window == window_encrypt and event == 'Encrypted':
        
        if values['-PasswordText-'] != '':
            password_encrypt = encrypt_pass(values['-PasswordText-'])
            window['-PasswordEncrypt-'].update(password_encrypt)
            
        else:
            sg.popup('    Por favor, Digite uma senha', title='Aviso')
            
    if window == window_decrypt and event == 'Decrypted':
        
        if values['-PasswordEncryptFunc-'] != '':
            password_decrypted = decrypt_pass(values['-PasswordEncryptFunc-'])
            window['-PasswordDecrypt-'].update(password_decrypted)
        else:
            sg.popup('    Por favor, Digite uma senha', title='Aviso')
    
    if window == window_encrypt and event == 'Copy':
        copy(values['-PasswordEncrypt-'].rstrip())
    
    if window == window_decrypt and event == 'Paste':
        text_copy = paste()
        text_copy = text_copy.strip()
        window['-PasswordEncryptFunc-'].update(text_copy)
        password_decrypted = decrypt_pass(text_copy)
        window['-PasswordDecrypt-'].update(password_decrypted)
