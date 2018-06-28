from .format import format


class Klasa_html(format):
    
    def czytaj(self,dane):
        html=[]
        b=False
        for a in dane:
            if '<body>' in a:
                b=True
            if '</body>' in a:
                b=False
                if b==True:
                    html.append(a)
        return '\n'.join(html)
            
        
 # dane=[{},{},{},{}] 
       
    def write(self,nazwa_pliku,dane):
        p_html='''
        <html>
        <head>
        </head>
        <body>
        '''
        fields = dane[0].keys()
        strona = []
        strona.append(p_html)
        strona.append('<thead>')
        for field in fields:
            strona.append('<th>'+field+'</th>')
        strona.append('</thead>')
        table_k='</table>'
        for a in dane:
            strona.append('<tr>')
            for key in fields:
                linia='<td>'+dane[key]+'</td>'
                strona.append(linia)
            strona.append('</tr>')
            
        k_html='''
        </body>
        </html>
        ''' 
        strona.append(table_k)
        strona.append(k_html)
        with open(nazwa_pliku,'w') as f:
            f.write('\n'.join(strona))