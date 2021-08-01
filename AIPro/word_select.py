import os
import pandas as pd
class Word():
    def __init__(self):
        self.file = self.init_file()


    def init_file(self):
        p = os.path.dirname(__file__)

        file_path = os.path.join(p,"configs")

        dirs = os.listdir(file_path)
        df_list = []
        print(dirs)
        for f in dirs:
            print(file_path+"/"+f)
            z = pd.read_excel(file_path+"/"+f, engine='openpyxl')
            a = z[["intent","话术",]]

            df_list.append(a)
            return pd.concat(df_list).reset_index(drop=True)

    def init_new_file(self, txt):

        df = self.file
        df.columns = ["intent","content"]

        df = df.reset_index(drop=True)

        print("df.intent = ", df.intent.tolist())
        intent_df = df[
            df.intent == txt
            ]


        if txt not in df.intent.tolist() and txt:
            txt = "无法识别"
            intent_df = df[
                df.intent == txt
            ]

        print(intent_df.content.sample().iloc[0])

        return intent_df.content.sample().iloc[0]
word = Word()
if __name__ == '__main__':
    word = Word()
    word.init_new_file()