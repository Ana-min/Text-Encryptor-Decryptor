from flet import *


custom_encryption_map = {

   # Uppercase Letters
    'A': '∆√∫∏∑≅≆≇≈≉', 'B': '∑∏πΩ℧ℨ℩KÅℬℭ', 'C': 'Ω≈ç∂ƒ©ªº∆√∫∏', 'D': '∂ƒ©ªº∆√∫∏∑≅', 'E': '†‡µ¶•§†‡µ¶•§',
    'F': '∞∩∪∧∨⊕⊗⊥⊿⋅⋆', 'G': '≡±≥≤≠÷≅≆≇≈≉', 'H': '≤≠÷≅≆≇≈≉≡±≥', 'I': '◊♠♣♥♦♫♪♯♭↔', 'J': '♥♦♫♪♯♭↔↕↑→↓',
    'K': '♪♯♭↔↕↑→↓←∝∧', 'L': '↔↕↑→↓←∝∧∨⊕⊗', 'M': '→↓←∝∧∨⊕⊗⊥⊿⋅', 'N': '∝∧∨⊕⊗⊥⊿⋅⋆⌂⌇', 'O': '⊕⊗⊥⊿⋅⋆⌂⌇⌘⌥⌦',
    'P': '⊿⋅⋆⌂⌇⌘⌥⌦⌫⎈⎇', 'Q': '⌂⌇⌘⌥⌦⌫⎈⎇⎌⍟⍎', 'R': '⌥⌦⌫⎈⎇⎌⍟⍎⍫⍱⍲', 'S': '⎈⎇⎌⍟⍎⍫⍱⍲⍴⍵', 'T': '⍟⍎⍫⍱⍲⍴⍵⍳⍷⍸',
    'U': '⍱⍲⍴⍵⍳⍷⍸⍹⍺⎕', 'V': '⍵⍳⍷⍸⍹⍺⎕⏢⏚⏛', 'W': '⍸⍹⍺⎕⏢⏚⏛⏧⏦⏨', 'X': '⎕⏢⏚⏛⏧⏦⏨⏩⏪⏫', 'Y': '⏛⏧⏦⏨⏩⏪⏫⏬⏭⏮',
    'Z': '⏨⏩⏪⏫⏬⏭⏮⏯⏰⏱',


   # Lowercase Letters 
    'a': 'ⓐⓑⓒⓓⓔⓕⓖⓗⓘⓙ', 'b': 'ⓚⓛⓜⓝⓞⓟⓠⓡⓢⓣ', 'c': 'ⓤⓥⓦⓧⓨⓩ⓪❶❷❸', 'd': '❹❺❻❼❽❾❿➀➁➂', 'e': '➃➄➅➆➇➈➉➊➋➌',
    'f': '➍➎➏➐➑➒➓➔➘➙', 'g': '➚➛➜➝➞➟➠➡➢➣', 'h': '➤➥➦➧➨➩➪➫➬➭', 'i': '➮➯➱➲➳➴➵➶➷➸', 'j': '➹➺➻➼➽➾➿⤀⤁⤂',
    'k': '⤃⤄⤅⤆⤇⤈⤉⤊⤋⤌', 'l': '⤍⤎⤏⤐⤑⤒⤓⤔⤕⤖', 'm': '⤗⤘⤙⤚⤛⤜⤝⤞⤟⤠', 'n': '⤡⤢⤣⤤⤥⤦⤧⤨⤩⤪', 'o': '⤫⤬⤭⤮⤯⤰⤱⤲⤳⤴',
    'p': '⤵⤶⤷⤸⤹⤺⤻⤼⤽⤾', 'q': '⤿⥀⥁⥂⥃⥄⥅⥆⥇⥈', 'r': '⥉⥊⥋⥌⥍⥎⥏⥐⥑⥒', 's': '⥓⥔⥕⥖⥗⥘⥙⥚⥛⥜', 't': '⥝⥞⥟⥠⥡⥢⥣⥤⥥⥦',
    'u': '⥧⥨⥩⥪⥫⥬⥭⥮⥯⥰', 'v': '⥱⥲⥳⥴⥵⥶⥷⥸⥹⥺', 'w': '⥻⥼⥽⥾⥿⦀⦁⦂⦃⦄', 'x': '⦅⦆⦇⦈⦉⦊⦋⦌⦍⦎', 'y': '⦏⦐⦑⦒⦓⦔⦕⦖⦗⦘',
    'z': '⦙⦚⦛⦜⦝⦞⦟⦠⦡⦢',



    # Numbers 
    '0': '⓪➀➁➂➃➄➅➆➇➈', '1': '➉➊➋➌➍➎➏➐➑➒', '2': '➓➔➘➙➚➛➜➝➞➟', '3': '➠➡➢➣➤➥➦➧➨➩', '4': '➪➫➬➭➮➯➱➲➳➴',
    '5': '➵➶➷➸➹➺➻➼➽➾', '6': '➿⤀⤁⤂⤃⤄⤅⤆⤇⤈', '7': '⤉⤊⤋⤌⤍⤎⤏⤐⤑⤒', '8': '⤓⤔⤕⤖⤗⤘⤙⤚⤛⤜', '9': '⤝⤞⤟⤠⤡⤢⤣⤤⤥⤦',



    # Special Characters 
    '!': '‼⁉❕❢❣❤❥❦❧❨', '@': '✉✍✎✏✐✑✒✓✔✕', '#': '✖✗✘✙✚✛✜✝✞✟', '$': '✠✡✢✣✤✥✦✧✨✩', '%': '✪✫✬✭✮✯✰✱✲✳',
    '^': '✴✵✶✷✸✹✺✻✼✽', '&': '✾✿❀❁❂❃❄❅❆❇', '*': '❈❉❊❋❍❏❐❑❒❖', '(': '❘❙❚❛❜❝❞❟❠❡', ')': '❢❣❤❥❦❧❨❩❪❫',
    '-': '❬❭❮❯❰❱❲❳❴❵', '_': '❶❷❸❹❺❻❼❽❾❿', '+': '➀➁➂➃➄➅➆➇➈➉', '=': '➊➋➌➍➎➏➐➑➒➓', '{': '➔➘➙➚➛➜➝➞➟➠',
    '}': '➡➢➣➤➥➦➧➨➩➪', '[': '➫➬➭➮➯➱➲➳➴➵', ']': '➶➷➸➹➺➻➼➽➾➿', ':': '⤀⤁⤂⤃⤄⤅⤆⤇⤈⤉', ';': '⤊⤋⤌⤍⤎⤏⤐⤑⤒⤓',
    '"': '⤔⤕⤖⤗⤘⤙⤚⤛⤜⤝', "'": '⤞⤟⤠⤡⤢⤣⤤⤥⤦⤧', '<': '⤨⤩⤪⤫⤬⤭⤮⤯⤰⤱', '>': '⤲⤳⤴⤵⤶⤷⤸⤹⤺⤻', ',': '⤼⤽⤾⤿⥀⥁⥂⥃⥄⥅',
    '.': '⥆⥇⥈⥉⥊⥋⥌⥍⥎⥏', '?': '⥐⥑⥒⥓⥔⥕⥖⥗⥘⥙', '/': '⥚⥛⥜⥝⥞⥟⥠⥡⥢⥣', '\\': '⥤⥥⥦⥧⥨⥩⥪⥫⥬⥭', '|': '⥮⥯⥰⥱⥲⥳⥴⥵⥶⥷',
    '~': '⥸⥹⥺⥻⥼⥽⥾⥿⦀⦁', '`':'⦂⦃⦄⦅⦆⦇⦈⦉⦊⦋', ' ': '⦠⦡⦢⦣⦤⦥⦦⦧⦨⦩',
}

custom_decryption_map = {v: k for k, v in custom_encryption_map.items()}

def main(page:Page):
    page.title = 'Encryption Program'
    page.horizontal_alignment = 'center'
    page.vertical_alignment = 'center'
    page.theme_mode = 'dark'
    page.window.width = 500
    page.scroll = 'auto'

    input_text = TextField(
        label = 'Enter Text',
        multiline = True,
        width = '400',
        border_radius = 10,
        text_style = TextStyle(size = 16)
    )

    output_text = TextField(
        label = '########',
        multiline = True,
        width = '400',
        border_radius = 10,
        read_only = True,
        text_style = TextStyle(size = 16)
    )

    def encrypt_text(text):
        if not input_text.value.strip():
            page.snack_bar = SnackBar(Text ('Please Enter Some Text'), bgcolor = 'red')
            page.snack_bar.open = True
            page.update()
            return
        
        encrypted_text = ''.join(custom_encryption_map.get(char, char) for char in input_text.value)
        output_text.value = encrypted_text
        page.update()

    def decrypt_text(text):
        if not input_text.value.strip():
            page.snack_bar = SnackBar(Text('Please Enter Some Text'), bgcolor='red')
            page.snack_bar.open = True
            page.update()
            return

        encrypted_text = input_text.value
        decrypted_text = ''

        # Split the encrypted text into 10-symbol chunks
        i = 0
        while i < len(encrypted_text):
            # Take the next 10 symbols as a chunk
            chunk = encrypted_text[i:i+10]
            # Map the chunk to its original character
            decrypted_char = custom_decryption_map.get(chunk, chunk)  # If not found, keep the chunk as-is
            decrypted_text += decrypted_char
            i += 10  # Move to the next chunk
        
        output_text.value = decrypted_text
        page.update()

    def copy_text(text):
        if not output_text.value.strip():
            page.snack_bar = SnackBar(Text('There is not any text to copy'), bgcolor = 'red')
            page.snack_bar.open = True
            page.update()
            return
        page.set_clipboard(output_text.value)
        page.snack_bar = SnackBar(Text ('Text Copied'), bgcolor = 'green')
        page.snack_bar.open = True
        page.update()

    Encrypt_button = ElevatedButton(
        text = 'Encrypt',
        bgcolor = '#FF0000',
        color = 'white',
        icon = Icons.LOCK,
        on_click = encrypt_text
    )

    Decrypt_button = ElevatedButton(
        text = 'Decrypt',
        bgcolor = '#FF0000',
        color = 'white',
        icon = Icons.LOCK_OPEN,
        on_click = decrypt_text
    )

    Copy_button = ElevatedButton(
        text = 'Copy The Text',
        bgcolor = '#FF0000',
        color = 'white',
        icon = Icons.CONTENT_COPY,
        on_click = copy_text
    )

    page.add(
        Container(
            alignment = alignment.center,
            expand = True,
            content = Image(src='I Am Me.jpg',width = 300, height = 300)
        ),

        Container(
            alignment = alignment.center,
            expand = True,
            content = Column(
                [
                    input_text,
                    output_text,
                    Row([Encrypt_button, Decrypt_button], alignment= MainAxisAlignment.CENTER),
                    Row([Copy_button], alignment= MainAxisAlignment.CENTER)
                ],
                alignment = alignment.center,
                horizontal_alignment = CrossAxisAlignment.CENTER,
                spacing = 20
            )
        )
        
    )

if __name__ == '__main__':
    app(target = main)



