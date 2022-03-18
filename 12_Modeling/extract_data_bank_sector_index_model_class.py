#### sector ratio index class function



from pandas import to_numeric, concat

class sector_ratio():

    param = (
        ('symbol', 'kbank')
    )

    def __init__(self):
        self.df[('{}_multiple_P/E').format(symbol)] = self.df['P/E'] * self.df['MarketCap']        
        self.df[('{}_multiple_PEG').format(symbol)] = self.df['PEG'] * self.df['MarketCap']   
        self.df[('{}_multiple_P/BV').format(symbol)] = self.df['P/BV'] * self.df['MarketCap']


    def float(self):
        self.df['PEG'] = self.to_numeric(self.df['PEG'], errors= 'coerce')

    def dropna(self):
        self.df.dropna()

######## จะ concat ยังไง จะเก็บ data เข้ามาหลายๆอันยังไง หรือ class นี้เขียนแค่นี้
#######  แล้วเขียน class ใหม่ที่ใช้เป็นการดึงข้อมูลจาก class นี้ ไป concat และคิดกับ avg marketcap 

    def next(self):
        self.df = concat([])
        
    



def sector_ratio_index(df, symbol=''):

    df['PEG'] = to_numeric(df['PEG'], errors= 'coerce')

    df.dropna()

    #method 1, use string format
    df[('{}_multiple_P/E').format(symbol)] = df['P/E'] * df['MarketCap']

    ### method2 ใช้ string+string direcly
    #df[( symbol+ '_'+ 'P/E_weight')] = df['P/E'] * df['MarketCap']

    ### method3 use f'{df=}'.split('=')[0] 
    ######### มันเขียนเป็น df ออกมา ไม่เหมาะกับสิ่งที่ต้องการ
    #df[(f'{df=}'.split('=')[0] + 'P/E_weight')] = df['P/E'] * df['MarketCap']
    
    #df['P/E_weight'] = df['P/E'] * df['MarketCap']
    df[('{}_multiple_PEG').format(symbol)] = df['PEG'] * df['MarketCap']
    df[('{}_multiple_P/BV').format(symbol)] = df['P/BV'] * df['MarketCap']


    return df



kbank['Symbol'] = 'KBANK'
kbank = kbank.set_index('Symbol', append= True).unstack('Symbol')
kbank = kbank.swaplevel(axis=1)