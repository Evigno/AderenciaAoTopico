import os
import unittest

# texto de uma redação sem tags e sem trechos corrigidos. Aqui a redação contém os erros originais do aluno
# contem o titulo e o corpo da redacao
redacao_sample = """A Aids ainda não acabou
O vírus HIV é o assassino de grandes nomes como Cazuza e Freddie Mercury. 
A síndrome da imunodeficiência adquirida (AIDS), causada por ele, é um mal que ataca o sistema imunológico das vítimas e acabou com milhares de vidas no último século. 
Com a descoberta de medicações que controlavam a doença, porém o medo que assolava a sociedade diminuiu, gerando um descaso sobre um assunto tão perigoso. 
É necessário ressaltar que a falta de preocupação da nova geração em relação a AIDS deve-se principalmente a não ter havido um contato dela com o sofrimento causado pela epidemia inicial da doença, com auge nas décadas de 80 e 90. 
Pelo contrário, os jovens cresceram em meio a notícias sobre os milagrosos remédios que permitiram o controle desta , além de uma notável diminuição das campanhas que favoreceu ainda mais a despreocupação. 
O problema é que esta juventude esquece-se do efeito apenas amenizador dos coquetéis. 
De fato, estes não curam a doença apenas retardam seus danos e, mesmo com o seu uso, a AIDS é muito devastadora e a própria química forte dos remédios tem efeitos negativos sobre o organismo, mas em escala muito menor que a enfermidade. 
Mesmo com esses problemas, a banalização da doença é frequente e gera irresponsabilidades, como não usar preservativos. 
A principal desculpa para não usar-se camisinha é a confiança no parceiro, porém, ele pode ter contraído o HIV anteriormente e não saber, pois, às vezes, o vírus permanece no corpo por anos antes da doença se manifestar. 
Com a efemeridade dos relacionamentos atuais, há casos onde a pessoa tem relações com muitas outras, espalhando a doença antes de descobrir que a tem. 
Portanto, o fato de conhecer o outro e a aparência saudável deste não fazem uma relação sexual ser necessariamente segura.
Enquanto a ciência, que tem trabalhado arduamente, não encontra a cura e a vacina da Aids é fundamental alertar a população, por meio de campanhas na mídia e nas escolas, a fim de impedir que o descaso e a falta de informação espalhem mais ainda esse mal.
"""

# competencia:  Compreender a proposta da redação e aplicar conceito das várias áreas de conhecimento para desenvolver o tema,
# dentro dos limites estruturais do texto dissertativo-argumentativo.
nota_sample = 2.0

# titulo + corpo do tema de redacao
prompt_sample = """
A Aids não é mais a mesma? Por que diminuiu o medo da doença?

Em 1989, quando o cantor Cazuza assumiu estar com Aids, o Brasil ainda não sabia muita coisa sobre a doença. 
Assustada, a população precisou discutir abertamente assuntos como fidelidade, comportamentos sexuais, drogas, transfusão de sangue, e tomar atitudes de precaução contra o mal que destruía famosos e anônimos por todo o mundo. 
Com o passar dos anos, as discussões sobre Aids perderam o destaque, em parte pelo surgimento de drogas que prolongam a vida dos doentes, em parte pelo distanciamento temporal entre a juventude atual e as primeiras vítimas fatais. 
Hoje, o governo declara que a situação está estabilizada, mas a cada ano, cerca de 35 mil brasileiros se infectam. 
Estima-se que, no país, haja mais de 600 mil infectados, dos quais cerca de 230 mil não sabem, ainda, que são soropositivos. 
Apesar disso, muitos jovens descuidam-se, principalmente em relação às práticas sexuais desprotegidas, pois declaram não ter medo da Aids. 
Como entender esse comportamento?
O que falta à população para entender os riscos que essa doença ainda representa?
"""

class TestPromptAderencia(unittest.TestCase):
    def test_leitura_prompt(self):
        redacao_dir = "a-aids-nao-e-mais-a-mesma-por-que-diminuiu-o-medo-da-doenca"

        # a funcao deve ter o caminho da redação e o caminho para o prompt
        # e deve retornar o texto puro dos
        redacao, nota, prompt = leitura_redacao(os.path.join(redacao_dir,"xml","a-aids-ainda-nao-acabou.xml"),
                        os.path.join(redacao_dir,"prompt.xml"))



        self.assertEqual((redacao, nota, prompt), (redacao_sample, nota, prompt))  # add assertion here


if __name__ == '__main__':
    unittest.main()
