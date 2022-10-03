
def main(text):
    text = text.replace("tg", "tan")
    text = text.replace("ctg", "cot")
    text = text.replace("÷", "/")
    text = text.replace("**", "^")
    text = text.replace("atg", "atan")
    text = text.replace("actg", "acot")
    text = text.replace("lg", "log10")

    #root()
    #тут є недоработка, що не працює корінь всередині кореня по типу root(3, 2^(2.6) - root(2))
    for i in range(text.count("root")):
        if "root" in text:
            a=text.find("root")
            koma = text.find(',', a)
            b = text[text.find("(", a)+1:koma]
            #c = text[koma+1:text.find(")", a)]
            c = ''
            i = koma
            open_bracket_count = 1
            close_bracket_count = 0
            while i<len(text):
                if text[i] == "(":
                    open_bracket_count += 1
                elif text[i] == ")":
                    close_bracket_count += 1
                if open_bracket_count == close_bracket_count:
                    c = text[koma+1:i]
                    break
                i += 1
            text = text.replace(c, str("1/"+b), 1)
            text = text.replace(b, str(c), 1)
            text = text.replace("root", "pow", 1)
            print(text)

    return text
