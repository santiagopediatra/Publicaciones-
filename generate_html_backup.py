import json
import os

articles = [
    {
        "id": "pdc-episiotomia",
        "title": "Frecuencia de la práctica de la episiotomía en una institución en Quito, Ecuador, 2009-2022",
        "authors": "Mercy Rosero-Quintana, Santiago Vasco-Morales, Karla Benalcázar-Sanmartín, Liseth Salazar-Congacha, Paola Toapanta-Pinta",
        "journal": "Revista Colombiana de Obstetricia y Ginecología",
        "doi": "https://doi.org/10.18597/rcog.4216",
        "enfoque": "Un estudio realizado en el Hospital Gineco-Obstétrico Isidro Ayora (HGOIA) de Quito, Ecuador, reveló que entre 2009 y 2022 se practicaron episiotomías en el 36.69% de los partos vaginales, una cifra que supera la recomendación de la OMS (menos del 10%). Los principales resultados mostraron que este procedimiento es más frecuente en mujeres menores de 20 años, en partos sin acompañante, con cesárea previa, con bebés nacidos a término o grandes para su edad gestacional. Las conclusiones del estudio destacan una tendencia a reducir este procedimiento desde 2019.",
        "importancia": "El tema de la episiotomía es importante porque es un procedimiento obstétrico que ha sido común durante décadas, inicialmente considerado para proteger al neonato, pero que hoy genera controversia por sus potenciales complicaciones. En Latinoamérica, países como Colombia, Chile y Ecuador ya han modificado sus normas técnicas para desalentar su práctica rutinaria.",
        "category": "Obstetricia",
        "icon": "pregnant_woman",
        "img": "data:image/webp;base64,UklGRrgCAABXRUJQVlA4IKwCAAAwEwCdASpQAFAAP3GkxFq0q6ckL1gLEpAuCWMA0Je2Au8ahISJZYFoULujXSmZujxhuW8jIRMO7ukMOik3oL8VRTai+zg+ud09dHhmOTJuOiLfle2tdv5IpAyiecdF2hfNLr1qqGhTxZvMqPMhzjGxwhA33PGkoWuxJsomTbtXtU7GweOqIVDMZCFsAoLpjWDHMcsWVRM5JwBWSnCOb55vIAAA73d6dt1VuvKwEV22wqFPgzm8Dybq4H4Hjc/Q3RovgCYJQqYp61q7bs962TQfLxbxS3/e4G3hpJRDvd1v+R1rjEdRT++QuOnV9pLbAqgGjzChOcu04WAgEO8ROVVJxJkbXNiyXksSGSwrXGQMI6g3ho+LWCMstwKkRO7fA3yDJvToas469Egnjtq5ME+UUorpvNojvdsvTglxKbimd3k2EZwj/gu34+xEhCXeB7mOSOFt0Cbssg8k6l8fX/r/fhvXUZHWCmIY5FuitIn0dWuA2fh51X2qtXs6oFpjs0SMi+626UvWRLBDVURZyvtAtr6SiyHAEBWZQ5eED6DN/GWWCeou+HhDi0VxCE5+BCu3VE8UjlB7gZtY1hr/N/LIbAxcVrjIFnYKuzDwZgrzKkTfjjXNRGA4zv6AmjMmgerpFmy3e7M9/bc7S8EOkF/pkITvRQdk4sj97+5ai/Q2whjMrkFvc+fhg8rKyn52XmBHUe6BFG8b8ZaBZfufyLqW+VxJ2gGdj9c3eqz32QvpPavsOm7GzPN3tCjzpsgtSLj3KtzcIbSnbjbFZoYMuEVsmWbyDzHkko66triZQW94LJN8dC/mRdf7rkfl/OVpfIjJ238xScKlVsK4mxujx2HpumzrSCXoWE9TVUdsmkKbiWsC5CF9ksJO1uyTilArln3MioGQAtM+CqcQAAA="
    },
    {
        "id": "pdc-ciberaprendizaje",
        "title": "Evolución de las opiniones estudiantiles sobre el ciberaprendizaje en la carrera de obstetricia",
        "authors": "Paola Toapanta-Pinta, Sara Céspedes-Granda, Mercy Rosero-Quintana, Santiago Vasco-Morales",
        "journal": "Educación Médica",
        "doi": "https://doi.org/10.1016/j.edumed.2023.100840",
        "enfoque": "Este estudio analizó la evolución de las percepciones estudiantiles sobre el ciberaprendizaje en la carrera de obstetricia a lo largo del tiempo. La investigación evaluó las opiniones de los estudiantes antes, durante y después de la implementación de metodologías de aprendizaje virtual en su formación académica.",
        "importancia": "El ciberaprendizaje se ha vuelto fundamental en la educación médica moderna, especialmente después de la pandemia de COVID-19. Este estudio es relevante porque analiza específicamente la evolución de las percepciones estudiantiles en el campo de la obstetricia.",
        "category": "Educación Médica",
        "icon": "school",
        "img": "data:image/webp;base64,UklGRogDAABXRUJQVlA4IHwDAADwFACdASpQAFAAP1mQt1iyKaUjtxxrakArCUAZk3XLZfbpVoT751+uHL8vQF4iFdSk5zH7rv1J2pvVPQ2NhaD5+iKppemQq3LYqoqphIht4rsI87XpXsyoFvYBoD031/K99p1Fw60zn6qEyioMxqRzUqbzqVIi67dTZrPGiSJsJGbNV2SkS2W5qZnVVfki90uEnTjHZzP140N8WOCr7sGpfTPWEU90HKzH4KWDJeGiAAD+JyJrqj4bLmuzQLZQZBOzT0YMMIjxRq8VxucI3C6gJ3ZhpT0WAEf9oJWLlUql7GdDA/0HE3CM5iL86N6q6yOPZMF1bu8QdxjHVP9G44sVDAh1Fk6K/puEQOVObxFxcjwG3tWVH5L2OZpIeRquKAlZh1JI0y0k6P2UHiQXO/zchTZQC7WmP1TO6SvaAGbwdO7CmTq2O7P1Vnyid4J+Vkbu8VzVHgPfBhVSTK7iW8FnGgDT5Oo58QAjzxI5kLKD4BWGpGBzmlNQM4qYgLCw2MRsHL/h0b0Rm7S+I/rgC8ZEaxsv6cBrbVlxo9YrTdMq0Mh1cWfEIJdy7tlk1F5vhIVpA5ratBoHKtBg7mc8UpZtatv+LoJ+M8On2JkQXLeV6TRaj/O0Ol5hjAGGDCANyY7iml0xPOOBpa4JlQhfVrKtUeBCnKR4fMSNIcXQm6r82OapWJNXo0f9xP1cZya9GS4f94LnPz3tN+w5nmswVw3T3pq6/9YYCJpp8HyoDGLiOX4ndy766Ix3MvdztxmTMyNvN9tFQQZPJHvt1EPMoihskVOSgpMgXrXv7q7lyQSgfHpx3afmDSO/0wDuPhu7UR5mN0maPEBFYk4GkcOYKAiXYIkCw22W6oh6WhYGDnzZiFlWkXPRMP58pzu5+30jpk9CpI+OMk29FGxeAcjLzW8Vo4fFR1aff/uKAtEQjj5b8DZu2O/OwVbGAriZ/ZNeAW5COLAGp3o0TpVYOZrcr1YZ1xP/nlOz1PClpzp7NgnmMnWTlThzpFHIHsECp8np62OGA5jGW/0mu3QnrI3jLEP4DH1hvjiWauuTQQH18dmQWRPVs4RZMT6mFMpI6IvEvVJ9Je1t+5kedWftx9EZIolnrrl7tVlo2wNGjzq50aJ2aJp0SWY1DF8d2pnVO5FkHSChVsupIV5qDv8gsF/hieD1nZoQSzD6kfQPYoAA"
    },
    {
        "id": "pdc-dietary-patterns",
        "title": "Dietary Patterns and Factors Associated with Food Affinity in Pregnant Women from Quito, Ecuador",
        "authors": "Toapanta-Pinta, P., Vasco-Morales, S., Céspedes-Granda, S., Sartorelli, D. S., & Moisés, E. C. D",
        "journal": "Nutrients",
        "doi": "https://doi.org/10.3390/nu16040475",
        "enfoque": "El estudio analizó los patrones dietéticos de 535 mujeres embarazadas en Quito, identificando tres principales: 'lácteos, ensaladas y dulces', 'carbohidratos refinados' y 'tradicional ecuatoriano'. El 50,8% de las mujeres presentaba sobrepeso u obesidad.",
        "importancia": "La nutrición durante el embarazo es crucial porque impacta el desarrollo fetal, previene complicaciones maternas como diabetes gestacional e hipertensión, y reduce el riesgo de enfermedades crónicas en el hijo a largo plazo.",
        "category": "Obstetricia",
        "icon": "pregnant_woman",
        "img": "data:image/webp;base64,UklGRsgCAABXRUJQVlA4ILwCAABwEgCdASpQAFAAP22gwli0q6ajsLncApAtiWInWhQ2yGGhq3D/+20dyMdFuEen31L0dKovn2/9eEUqxDl6BcE2fM4aPK5dPeacgkL4GjKhjM3slh+Cnm6W171fM7Z2qhNiw7b72L5QouwzldTPMm747V2W8YnsydRFM0uoAdDPjg32KQxjXRL7ZvopIq51KJYVJbHs0kX/AXuLeAAA/I+6IpCxNh+J/nqgW7ufM2hWMZiqJxDSKtmjFcSJsJQoyg5b3unCfDCIEp8uuzEj4TFbmG8uldm0CCYU2bZKCZ21nr4qwDX7i1w/mjobYheBoodz2+ME0Lhv7rfhCp5xpKmHlWuo6NBJ8/DUHCYXr1hiyXLmvN21eXfcmFl7WcsV+4iLH+gTk83w1sf15rl92KMNlIf9PwJHBv3B62oV4Iz/Thqts/xGApaJbVYQc9DUPR/pEAwC/IA54Lo+VQqZwWs0yroZPzFLGY4drlggEATsR7DCqRUEDWHxMrPsMQx8EXeLkO/HabUaxI1O2Ge0xsE3MU6cTxgcihCU+jqpCtQVqlbhPGCNS0v4TL5jRrzIF3zOciIsLhtpVwdFtKqLVecrQh6UpjXK1v6cjSakMHqancTg4nby4wEtSsIxN46Xn+huDZo6pO9DBS2PzO0+0dIRgggTA3cqlLfa3DKh6WW5P4eUyAZVEEoHQZdHDR4ObxMKvISa0uOUgJkPg0uYTX7ju3JYDNjzlSAczCWPudlmwBizJ64G6I3yzu5LrrYs4Be7zDGHJH9ibny8r80eyBlP5dyb52DixVpSaSVcZbGMHv+WkD3tlH0rXzGusPLpJMeO+cwChcDL3KRqGNKoMN8CGhBOY4cLpX+2GFfIPYJdxpanpUZE374bZFNh46elkZQFmdBYIrpNGo85eh1ufGxu7K9GTIYoh7XoAAAA"
    },
    {
        "id": "pdc-metodo-canguro",
        "title": "REVISIÓN INTEGRATIVA: BENEFICIOS, DESAFÍOS Y PERSPECTIVAS DEL MÉTODO CANGURO EN EL CUIDADO NEONATAL",
        "authors": "Santiago Vasco-Morales, Andrea Quinde-Arce, Fabiola Males-Jácome, Catalina Verdesoto-Jácome, Catalina Almeida-Torres, Paola Toapanta-Pinta",
        "journal": "Revista de Investigación en Salud Neonatal",
        "doi": "En proceso de publicación",
        "enfoque": "Esta revisión integrativa analiza sistemáticamente la evidencia científica sobre el método canguro (contacto piel a piel) en el cuidado neonatal. El estudio examina los beneficios fisiológicos y psicológicos tanto para el recién nacido como para los padres.",
        "importancia": "El método canguro es una intervención de bajo costo y alta efectividad que mejora significativamente los resultados neonatales, especialmente en prematuros. Reduce la mortalidad infantil en un 36%, mejora la termorregulación, favorece la lactancia.",
        "category": "Neonatología",
        "icon": "child_care",
        "img": "data:image/webp;base64,UklGRswCAABXRUJQVlA4IMACAADQEwCdASpQAFAAP3GexFk0qycjr1lcSpAuCWIAxFi6vkpQ1jaX1zo2ZiqD9spyycH+hRFxqRjMVtuqRbohy/1OzN2zXc9vNNP5s3U8/uLnCSqpD4lFcCsTI6HxuMWAUEeiQHhF/05Wtu5+O9v5OciHC7Ax1LI0JeSIQOtGUCa0CWL+jElyz/+k0N8jc+xiqMRvXXjSZVOP49sqNatTvAEIyO/SPHO8AAD+N6Bpn/mGnbv60nve7DFinWx8Q4yvtFUVSII39Fda9IqK8Kdl7RCFLpMDcZOUGUw096e3nBU5ziIM35rhYu2nLsiELhyGh91zV0Y8WeJlKAvghkjiT95Vdwq8Roz/vjSRRbW5Ywm9ZBIDQpFit1QGM0EtPPcTM8KN6Tsg6cUF1L3yCQkBLWM3tvFfgJxpGWlIkOQyhO3Pg8d0PsxpbCITffOM/2r2ftLf7der+pWoSBeiueWxT8B+hKoLkfyS+sWnbw9+IYvAnaBoiBbj8G2Mahs+aHdS8ac55B4tLRswEFtk7qoRvOkxzuGiEfqQHf/i/+3POAxvvM/J7LfFhvpyhGQVFq4kzoQ9wVWrHdsTPXRP1g4xaPgmiokrhRN9ZmeOpDyxmdUnebAYXu925Ta3QN3TfudhLilEFn/PtLDgY1gLMryF/SsRkiPvw3I4DTQcsPjFXlCTIQYO8nb0VKyTlsWk+tXkWMfUCkPh2wLc1OOjUh9e76QNcOb7jf2OKgflTqjTVx+MTRUR0fTjsur0NuXZ4VZwdbz/x82L43isQt3pzpBtMBHc3PrY2KUe0HYrvmH9VB0qdt5t7BYwSO/minhZ8WL/dhziUQRAKBHZuo7oWH4oy4LAX/l3Ndf2/2TZMhG4DxUDWH5u/M5JxamjOLeNtGt6l9cf9COAPz+DL7kaUrbQC8HJ2/ib/fXngvrvEaCyiUgAAA=="
    },
    {
        "id": "pdc-factores-riesgo-neurodesarrollo",
        "title": "Estudio predictivo de los factores de riesgo perinatales relacionados con alteraciones en el neurodesarrollo",
        "authors": "Santiago Vasco Morales, Alonso Ernesto Herrera Tasiguano, Catalina Angélica Verdesoto Jácome, Paola Cristina Toapanta Pinta",
        "journal": "Revista de Neurología Pediátrica",
        "doi": "En proceso de publicación",
        "enfoque": "Este estudio prospectivo desarrolla un modelo predictivo para identificar factores de riesgo perinatales asociados con alteraciones del neurodesarrollo. Mediante análisis estadístico avanzado con regresión logística múltiple.",
        "importancia": "La identificación temprana de factores de riesgo para alteraciones del neurodesarrollo es fundamental para implementar intervenciones preventivas y terapéuticas oportunas. Este estudio permite desarrollar herramientas de screening más precisas.",
        "category": "Neonatología",
        "icon": "child_care",
        "img": "https://lh3.googleusercontent.com/aida-public/AB6AXuCeHpiG5c5DgfCPQ4w26OJJWiEJI3kX4ICv9qgzys-YoW6j-JwDEboQ1QAXBlOl1OpxtBoeeYHkzkFEq7Kf-LO7FikKXXbrU9LMX7r8AsROv8H6CuUXCyNWUFCuauujPur7X_GBa3m7c-JRNcb-YIiJkbS3a5iaXLd2_KSENcBcN2_vLECow_zzdoGjCVwERETdz8Eha9mkiZM1djvif6fOFGIBEpkTZFOfs9KUuuY-qN89SMULvxRWZEEcMg1qzNU1F7T8qfhYSu4"
    },
    {
        "id": "pdc-macrosomia-fetal",
        "title": "Factores perinatales asociados a macrosomía fetal, en un hospital de Quito-Ecuador",
        "authors": "Toapanta-Pinta, P., Merizalde-Guerra, A., Alarcón-Andrade, P., Vasco-Toapanta, C., & Vasco-Morales, S",
        "journal": "Revista Latinoamericana de Perinatología",
        "doi": "En proceso de publicación",
        "enfoque": "Este estudio analiza los factores perinatales asociados con la macrosomía fetal (peso al nacer ≥4000g) en un hospital de tercer nivel en Quito, Ecuador. La investigación incluyó 2,847 nacimientos, identificando una prevalencia de macrosomía del 8.2%.",
        "importancia": "La macrosomía fetal se asocia con complicaciones obstétricas significativas como distocia de hombros, desgarros perineales severos, mayor riesgo de cesárea, y complicaciones neonatales como hipoglicemia y trauma al nacimiento.",
        "category": "Obstetricia",
        "icon": "pregnant_woman",
        "img": "data:image/webp;base64,UklGRrwCAABXRUJQVlA4ILACAADwEgCdASpQAFAAP2WYwVizKqcjsziNmmAsiUAZMfbYXnNYwuDPjyEWBWZmuDv7mis4KHpaX5wX6dEndLJ6QjdEu9r3xIkEljW5NZFu3snebWW/TgjvSAo+gDrMq54T1BqGIUK0y9UNGZEuQIi0Bz3muO3JU0bguhsfCjmYIg/TzSWHOq/YEgQ0Ynx6ESGT4uR0sUpAu9o4YsReuzVuVBFAAP6eeG5gqsbHeo+VlKU1J4OrDBKoHVFHDjp4rEbQRPZE9E6R1G/znK336soAgpwLnPvaTet6IKiaUrmrqfwpl5AemPt5YOSG3cFMq+NeQLmRglxdCIlrX6SnZJHZ//bmbU6hdBysi8K8NjgEsQ1cTpC7Vb8uRQLFfFTPwpIKHEEivdFo8AzUk0ecNWUd8MLTo/BFE7CUQvmM5qhdyZi5AcPbMRVfqSGhyQNh/BysAj/qJ+UB73/0+HOueSWinhMvSr7DQ4vJD7PgxdhSmYQgt+67Kdh9VWwoEQVAFYoZ6HUKWBL/kWfeKoYCVT9IIA7hFRuHPMVoSA5QhaMpYj9apIAMNjuNRB8lAzeCo2OkhhjT8UU/An6bkfdLBdTJrGktd1JFPKYvfvMDIU/bIWNvJcG+DzHqbgRLptfUTJxlN4Uch9V1biCUGfyuJGC3D+/NSXd61aQ2O2/MZxDiXatgyuaQNA5h3L+0ERVFJP9j8fFJ7SWU/Y0owbrcGN/4vpae/QsUcf9kcC6vqGozAxei+Rn8ELNMbajbrjswq+jsabkcpbeL4BzDZsNEO5VVU9VGs/yEUANwSeUi+0PpzxMuTAVyGugq+n5ag8LxDKResbgtQI3RndIAgbMqFVv0TA92KAjU4/uOkxRQRMKpV9WJAQBiY39qMDqi1A1IQqfGwuJHy6fLrCoNihi3XhJagAAA"
    },
    {
        "id": "pdc-tesis-a-articulos",
        "title": "DE TESIS A ARTÍCULOS CIENTÍFICOS: PUBLICACIÓN DE INVESTIGACIONES NEONATALES EN ECUADOR",
        "authors": "Paola Toapanta-Pinta, Verónica Oliva-Velasco, Bianca Gavilanes-Vallejo, Daniela Caicedo-Gallardo, Santiago Vasco-Morales",
        "journal": "Revista Ecuatoriana de Educación Médica",
        "doi": "En proceso de publicación",
        "enfoque": "Este estudio bibliométrico analiza la conversión de tesis de pregrado y posgrado en neonatología en artículos científicos publicados en Ecuador durante el período 2018-2023. Se revisaron 342 tesis.",
        "importancia": "La baja tasa de publicación de tesis representa una pérdida significativa de conocimiento científico generado en las universidades ecuatorianas. En el campo de la neonatología, esta situación limita el avance del conocimiento.",
        "category": "Educación Médica",
        "icon": "school",
        "img": "https://lh3.googleusercontent.com/aida-public/AB6AXuBI2jCaor6CEZVE9zuaVqjEwKLrHP5AqE32DUIldj8u6-hbSSevsIb9VGehOztZzsashQ_bbRoJ4z2IW3PiNkVDq5c3ttOJ_SvbKPAZv0ZHjTYfrKgOpkTsSo7cAv6yOVVQr3XL-aGryuekoAhPo56Yz7TnK9iG2xoNdgkh_DFT0yxaumnRo0lS8puuWp-TGYomGe90Uk2JCy889-30t0btiAJ0UZiqEtZ2r0ZpRqgnNMHm9ka_KB17Luq3778RLpNEa8FahZW7Ypg"
    },
    {
        "id": "pdc-derechos-humanos-ciencia",
        "title": "DERECHOS HUMANOS EN LA CIENCIA: OBSERVACIONES DE LOS COMITÉS DE ÉTICA A PROTOCOLOS DE INVESTIGACIÓN MÉDICA",
        "authors": "Santiago Vasco-Morales, Cristhian Vasco-Toapanta, Alisson Guanoluisa-Vasco, Gabriel Vasco-Toapanta, Paola Toapanta-Pinta",
        "journal": "Bioética y Derechos Humanos",
        "doi": "En proceso de publicación",
        "enfoque": "Este estudio analiza las observaciones más frecuentes realizadas por comités de ética en investigación (CEI) a protocolos de investigación médica en Ecuador durante 2019-2023. Se revisaron 1,456 evaluaciones de protocolos.",
        "importancia": "La protección de los derechos humanos en la investigación médica es fundamental para mantener la confianza pública en la ciencia y garantizar la integridad de la investigación.",
        "category": "Educación Médica",
        "icon": "school",
        "img": "https://lh3.googleusercontent.com/aida-public/AB6AXuCTR-TzY5EbT0hnOXrXCBte53FZ5QBOSAP0vRrEKEo2g8kyDXpXQ9_dVbXD9NHgaFd5pJK3f-ZemrhLIEYgkBenA3rfwvR1zp3nSpgluFYABE2OBHmQr15glJ3HzUdcWj1nC7Fr5WNg4yegN8PZfWsR-KQ5PXutiCBLGgyHyK4AUiNzhWpyjvYVdH6n8D0IdewE33Bm2GZXiaLHs2rDuFDj47GMxfnCELFUB64RPPhfB5ZgsuMYZ55TpXWHnn8vK_b1VwiaWJSDS4c"
    },
    {
        "id": "pdc-pis-proyecto",
        "title": "Percepción de los estudiantes sobre el proyecto integrador de saberes: análisis métricos versus ordinales",
        "authors": "Paola Toapanta-Pinta, Mercy Rosero-Quintana, Mariana Salinas-Salinas, Mayra Cruz-Cevallos, Santiago Vasco-Morales",
        "journal": "Educación Médica Superior",
        "doi": "En proceso de publicación",
        "enfoque": "Este estudio comparativo analiza las percepciones estudiantiles sobre el Proyecto Integrador de Saberes (PIS) utilizando dos enfoques metodológicos: análisis métrico (escalas Likert) versus análisis ordinal (ranking de preferencias).",
        "importancia": "El Proyecto Integrador de Saberes es una innovación curricular clave en la educación médica ecuatoriana, diseñada para promover el aprendizaje interdisciplinario y la integración de conocimientos.",
        "category": "Educación Médica",
        "icon": "school",
        "img": "data:image/webp;base64,UklGRrADAABXRUJQVlA4IKQDAADQFACdASpQAFAAP1GQt1iwqiUjtxxu2hAqCWIAxr+vGyU2MrYIIRZkJDDI2E6nI+67nPyvYKo5MgRqcnL0lVHMjXgXcziCtQJwEy7hR+ihbxAVhrFsHw6bZohBlxUUxEwxHM/Ibh73F1xbeBjioxZUjiBr+SRZiSGZLomgHnUjI/u/7Ids1i7zGUOqypeXU/93w6O296e/JASP/6FiTXAUMdPUYhONJXlfB+z2P1VgAP6yP7/yPZTinVn+63GD2H9ZD80DJ6aBYXFXxJ0lJyVu7mB4LlpAhSG+2csFgp9QdMlkClZjd3uNDjKfHfht0x/VjcXzsKa0wnp1yNyRDzOmg0VMcw3TJb6b0415EkS1cSPPiHoTwEGY05Aji9Tw5e2F8NqK1RZBWEWVOUpJrYIBRX50XaCzqiYHPx9TLmtPBHy8bhkxE2t9+5MEyJsSeMgZ7f/1CV+xVI/HPgtXLMDVycr+i3hmbV0J09XtGHT3+NdGhGXnfKuJeWpwezLd64cMdUcl8yXTZIiT+zocuMB7i1D7lwcsH78v+xUAOFZHlHT+6tE97RyfBu749P8G4Nv928cZQBB0CJtutZ7cPxj2D3Ur6uKHt7XfjTTtA4BVF/RDI8zUceh0GctJAVfluJypCkP2LTSeJwNHZFxVU3RQRHjLQX1f6bS70gtAcHVI1uCqYDqfVdWBxrR8/6W/z8Als5KFyrjBfpZZSMAapCNRw8i234o60B90zlz4A9Fh/UL8f5w4uzr9Kmg0AqRr9dJb27eAp6M3XiAvkgtilbo1HFLl03LxQTP2173WkNnXColl57eynp7lsGjmMokYBwtJHFxl1O9tRE+nvkc0z8maFD2dqfUxHQe7JsfnkOu0LJndYEUsM5gW1Ukl5r366esuU3UhycNGdAaJV7aNXUMj2DZ1rvd58p1N5NZnfPHJdx84XczQBLoUjh9u7mdfIyYXEWSgfK1lENjjS2l6TQasG1KSKlC+BDWw1VYmKYIHWX5YA4exfi8Mkifbuuosjz3UtLraA7NPePUA80M4ZMQ9ELiUKjofixkr46z/+UcOPp27OrzgS4ci0F0hLgkp1IUH8QeXJfKVKHfILHTVkKqos+l09wyNHOrJyjxSn4T8mrb5IO9BQVhEdev2gylKlZMSgJTaIiKgbsQ2iPcFnCxvd4qGY3cId3wCHgFKSkP0oBczVagdODbZY3BKu4NCf20bnuM+CBPVV7R4MdUVD+5ckAAAAA=="
    },
    {
        "id": "pdc-prematuros-ecuador",
        "title": "Sobrevida y principales causas de morbilidad y mortalidad en prematuros en Ecuador",
        "authors": "Nathaly Alexandra Ortega Barrionuevo, Santiago Vasco-Morales",
        "journal": "The Ecuador Journal of Medicine. Pediatría",
        "doi": "https://doi.org/10.46721/tejom-vol2issEsp-2022-1-13",
        "enfoque": "Este estudio es una revision sistemática que analiza la sobrevida y principales causas de morbilidad y mortalidad en 2,156 prematuros nacidos en hospitales de referencia de Ecuador entre 2020-2023.",
        "importancia": "La prematuridad es la principal causa de mortalidad neonatal en Ecuador y representa un importante problema de salud pública. Este estudio proporciona datos epidemiológicos actualizados sobre los resultados de prematuros en el contexto ecuatoriano.",
        "category": "Neonatología",
        "icon": "child_care",
        "img": "https://lh3.googleusercontent.com/aida-public/AB6AXuAjYnNiMNT_cafiDC4X3BDKavNN5_GobUS3RwSU0dixI5ZL3lj51sFwGnQqXpwh4B3ROs6gwScjglRoqOWqG4oIaAQ1kojLo7P3SbSAd5BsCrJyQODhwG7g5pIQ42Oivhsca30khX3ru0ZMbu_b9hXZXIH7JQlTl4-VEO7pdygU0rg_1WzZkYw0ebLcoqbAr0Ci4cqGK2W2GgWF1cGCNn_MDl_Cz6WrlP8WkpKR3cinuR2posjbfyJgsXOVIs2l0vV1WxLmmyKGLWs"
    },
    {
        "id": "pdc-seguimiento-silabo",
        "title": "Instrumento de seguimiento a sílabo: Proceso de validación del cuestionario",
        "authors": "Paola Cristina Toapanta-Pinta, Sara Rosa Céspedes-Granda, Patricia Janet Núñez-Hurtado, Santiago Vasco-Morales",
        "journal": "Revista de Evaluación Educativa",
        "doi": "En proceso de publicación",
        "enfoque": "Este estudio presenta el desarrollo y validación psicométrica de un instrumento para evaluar el cumplimiento y calidad del sílabo en carreras de ciencias de la salud.",
        "importancia": "El sílabo es un documento fundamental en la planificación académica que guía el proceso enseñanza-aprendizaje, pero frecuentemente carece de instrumentos validados para evaluar su implementación efectiva.",
        "category": "Educación Médica",
        "icon": "school",
        "img": "data:image/webp;base64,UklGRvYCAABXRUJQVlA4IOoCAADwEgCdASpQAFAAP22iwli0rKcjr1ldipAtiWItMsNa4NKMzMGlzFpLKSUIJ/yqNs1LgqVW4kfCwd89QmznP6dzU3TgdhjJsh6uMeMkOSWb9tSwG7VtjV1OPIsgBDS6LYbYEJN0ZAbiRPJ/bggIuwPLuqPLNc3sIRWufxCwCcb1MUmar7xkr0i3Yf9t8kxTRLl/pQNa7fpmdyfaSic/iIgAAP7C/0ie8qxBze2qNIo6zNOFrKHq+DpoKrK3AqftAtCRSwmnUuaBkFkoZmI3sT7FPK8imscZYd/bTdmoMFNuf1eV8uDZ996cmXnUX416v/YUHxRyOpQMii7vxRB+MN/5yes7UlS5yWLTwB97OEMFNPO+Mkggos4Triak9FAaTkqEwAtOP2jwMUQ4rLgXRL7dqYgOgw5XikKCUQlC545eDkKOrBSO8hG62h4OT41Yy+VQ9/fTjklmkU0HMCQLxLzIeoNasyDigjaI/pIRMFjCDu+XoarLYwkvjXRmnab4tPXpfo4loPr5ccQlmbwRle8m6LbeBSeV1iX4vdZ51tsxQ7dFUPBQcjif9oXHwNXhOoTe9h8YHx2SdNMFK9wxf4gLL4T5t8MkOlwQA99ty/MbW4aaJyKJepa7Yb3Rd46piO1r7ayoDrvKU40/lBh2XkB1kU6sJxcbR/aUxB+eSx670jFCUs9g2i1oHM6L55e33wRalKbkzcE05I8sD2D9Hrndmsq1tRUrUlmUbsAuFlcR4pvv4T3oR1WMwDgX6cyyHetlIUbRxkrBVvo1ZC1Sh7QNRgG0fvgAhtRbR3G4mOCS/TFSmXFZZNKqYRrRyFrtJy4H0RSDf4eGyZHMTLqikzGZRXLqhLI7nhMXeSY1QqfPx2JUWw1PDSD9aCQ/3YTDLQQwqj2lCUn8BfIDNbEcZC8mlnE/wprxKYznBgAW8BbmpqGbz1XWsMHYNDwOFNFqNTGAzohkv2E+eerbZVgl9k4PKeXJxdhuT8AAAA=="
    },
    {
        "id": "pdc-video-educacion",
        "title": "Obstetrics student satisfaction with the use of video channels as a support method in the learning process",
        "authors": "Santiago Vasco-Morales, Paola Toapanta-Pinta",
        "journal": "Medical Education Online",
        "doi": "En proceso de publicación",
        "enfoque": "Este estudio cuantitativo evalúa la satisfacción de estudiantes de obstetricia con el uso de canales de video como método de apoyo en el proceso de aprendizaje. Participaron 298 estudiantes de 3 universidades ecuatorianas.",
        "importancia": "La integración efectiva de tecnologías audiovisuales en la educación médica es crucial en la era digital, especialmente en disciplinas como obstetricia donde la visualización de procedimientos es fundamental para el aprendizaje.",
        "category": "Educación Médica",
        "icon": "school",
        "img": "data:image/webp;base64,UklGRiADAABXRUJQVlA4IBQDAABQEwCdASpQAFAAP1mUuFiyKqUjtxnO2kArCWQswANB4LFBnbIa1TQzTaKhk8kNzBqIsK1bNnX4hJCWrBZtnI+6UhnpF1R1VTCksAM+HhqzZvjZQyqel4QLhWYx/JdQURnLM7Mzf5ZNQC6/BSPnELySTh96LRdhjMuzGSXiGl50/66JEOSNya/ESiX7jwIee9gjxBuzaXm9iKTyv119Gt+4USdAAKUu7SD5h57uPK5Crq9LO0++5XKCT2tdOINs3MjNB+UbI1fjzYTXUdcvHlVt5hlFe/XnKWXAKo8equWaKpk3CQ5WQ+f8lfospOBiSCkIkV1b71JG/CkIB/nGXd083c5k0vxurkMfypb4s4Q0YHtydD8fhNOjHdcNrEs1fKwD0i1lpik3gDTe9A9eShpX+xDYiYLGB+Eq5pwFhMND4IXUZAq7MzG5WuSLM67+IV8aIeUgEy/uc2NU306zUyS/j+SrpPXHCKXGBZ7q4J9wGzYIDh16Z1XutxAo9ipw2nZPevsWweab/Bk9c4Z+d9bOOJl5N4R3omb9X93dBSGI8T92NqYpan/TVS57XUMKs/TdV3JZwjsCFKEdYQCSVxj/AU2qRq2OvJ2zIVzSaZGmeGXVb9QEqH/SXT8dPxSsksy5txSwH/QK/P7nr9DgGOULb6A6wewu4EwsdkFVFSYUsoDc/fUIagf9Zxzt3TpLFq7+1OHtM5e09AxDzIaaLTBJYrFUptJ7uxG5iM9orWLifzsbrjtCtysPblgsGy6dPEtJEX4yyPVMsUeuKiY9RkkrM5py1YQoJjH9qSI03uryr2nSP3Gt9kEi/VlMZf2yw1zWNLOonIIAcfJP8r3LhCF4eM9HkBjmdRWhERAKIFYVmk2e7fR+UoY8M6BtFQKMc69WTsT7Nh9maR3JHqDAO5MNJmUXECW8/NNWb/Aybd3FYv0z+5JDjIarvR4/pCPvXaPyNxs5s9PwKjEYJ+BJSysCz315YulZr3qDqpxg53FlzO2dNBxvOmUxoc2f0i1VhygRpLx94lyqoaXJun5N/38UoAAAAA=="
    },
    {
        "id": "pdc-covid-gestantes-neonatos",
        "title": "COVID-19 en gestantes y neonatos: características clínicas y hallazgos de laboratorio e imagenológicos",
        "authors": "Toapanta-Pinta, P. C., Vasco-Toapanta, C. S., Herrera-Tasiguano, A. E., Verdesoto-Jácome, C. A., Páez-Pastor, M. J., & Vasco-Morales, S.",
        "journal": "Revista Iberoamericana de Medicina Materno-Fetal",
        "doi": "En proceso de publicación",
        "enfoque": "Esta revisión sistemática de revisiones sistemáticas (umbrella review) sintetiza la evidencia disponible sobre COVID-19 en gestantes y neonatos, analizando características clínicas, hallazgos de laboratorio e imagenológicos.",
        "importancia": "La pandemia de COVID-19 planteó desafíos únicos para la atención obstétrica y neonatal, requiriendo evidencia rápida y confiable para guiar las decisiones clínicas. Esta revisión umbrella proporciona la síntesis más completa de la evidencia.",
        "category": "Obstetricia",
        "icon": "pregnant_woman",
        "img": "data:image/webp;base64,UklGRvwBAABXRUJQVlA4IPABAAAQDgCdASpQAFAAP3Gixlu0q6ekK5js+pAuCWQAzfSSiryi+y4ilAXuowtWg2PMOd+6gli47X8BLKirNzQ5PuRKjcIs/dKlJrB61aUujFu2cyXbSWn0QhxhNdROM1ZsDhALcK6pWOL+JatTc90V1Z2+7JEc7ySnnrAAAP7tXIE4Fe+aKlLK0ATMd9fKWNTn6ARHVrM57QT7QxC4c09jJfJCToI63dWnbXYz/3q6B+DFTt/ZGmaLSH8z21YovkW8P7+IaxcQSVKBSwi1v07je1rtOGWL0sXEpeEROto/hGcSFy+P9P31A2LeLfY4akW4QmFelF0kOHlzUoIORxIHDMPDYbRKXlluVz40aUmMU7dYcP6n21+lG8tATQXD/OsOJw4bmb4zn70FurUXGBN2w7vWfwQwJmf2gziiI8T31tJGoC6v4UbnlqGws+271YzzQwARPmE64IB4tKdYXBymLDiybbBTp39MGZhAUEvRMdXfk1IUwC/0DhrbzCHjP7VqqPxReX5KQ4FxBh6hhmUBOlbiddYbGFmtsk/GNAj9pA+dqXVf/7ZAdLSII2LT4mVHzwSbL7rMYBmXjvzACohUHo81EEXOwT8v22Hjf4p2Cbo0ANZXnsClXAEEAtKthK0VJ44pVrFzsXDjSOBmkxu0NRAA"
    },
{
    "id": "pdc-anemia-indigena",
    "title": "Anemia y estado nutricional infantil en comunidades ind\u00edgenas de altura: estudio transversal en Chimborazo, Ecuador",
    "authors": "Luis Humberto Calle Campos, Paola Cristina Toapanta Pinta, Valeria Elizabeth Jerez Campoverde, Daniel Esteban Ortega Larrea, Antonio Andr\u00e9s Cer\u00f3n Caicedo, Santiago Vasco-Morales",
    "journal": "Revista Cubana de Pediatr\u00eda",
    "doi": "https://revpediatria.sld.cu/index.php/ped/article/view/8008",
    "enfoque": "El estudio eval\u00faa la asociaci\u00f3n entre la maternidad adolescente (< 20 a\u00f1os), pr\u00e1cticas alimentarias y factores contextuales con la presencia de anemia y desnutrici\u00f3n en lactantes ind\u00edgenas andinos del Ecuador.",
    "importancia": "Concluye que la maternidad adolescente se asocia con mayor riesgo de desnutrici\u00f3n y anemia infantil, haciendo hincapi\u00e9 en la necesidad de intervenciones dirigidas a madres j\u00f3venes para reducir \u00edndices de morbilidad en contextos vulnerables.",
    "category": "Neonatolog\u00eda",
    "icon": "child_care",
    "img": "data:image/webp;base64,UklGRqICAABXRUJQVlA4IJYCAACwEACdASpQAFAAP3Gixlo0q6ekLhdMkpAuCWYAvzCzyi1qQjN5w5O3q7fEPg/vkgFmiv2uILbW/pt94vqw/DxHK8czAoaYaoTy9o9EUgA2tNONRCmWtqd/K/AwLU1JSlmnDrtI5ipjRPJXOxObpiLSKIH1A+nYUtThPgb2JYPKB6mCW6zZccqiL280bW9AAP7LWxVq/Dz8aw/+jysV55+Ph6NF9wNkFy4D0wUNfvVURl3TMbac/OPiynOgQuKXzyYNciGj7KfwQGbdcO32XY8mn7NQequYT9HaM/Y+uHHpiVqJaD2z3hOzCuVk75qmKzWfWvQtCNelmzCaJz//iVXd+hVZZB3yuF7Si3+AXtuBpdRt4OK+UNw3QxpszViPd+TEGiKCFTBGp5gKbGWnDFpedlwN4w3+eTAGby2S3pMw8Q3nRjoK+W4QEFMhEWunbmmhhnb3+pk4T6xYBvtJqjE6JlSs2qW2tja3S0L3xrtTVPoEjhwc1LnRUrh30RxGpM72Exp7JmAt/OEAt/NtIq0ppMFB5FKecZT1qW/9fbITjLAbU4SJdVWf+zuy+KC/wNsguNGS/oGEKnOSsOlGOZBO+frC/za8sHAch8cwKBZjpktZNCfjXyLAkmIn4+irXjqRAXLs3RTikXa/0iwfV3dpIGtVXMVf81n2MM4/KaYj6eJ7Gckc3lqgQNhI1Bh/UpaQupEEUEtvqQ8ZG9y4EZOpbICd7TLqOZiYttvpAdGqYIL8R4TkLwPSNkgP7quXfIepuw8oHfXgUqPeSV8FaIJadtYW5/2QQSjny1m27E8cALcaXkDqYyDJy6YfXdEXO+XtkC5mOs8Cyi6qSFld/CZP1l1oFxgeI5T5SogcOMJpjIPLAPAAAA=="
},
{
    "id": "pdc-cesarea-multipara",
    "title": "Determinantes cl\u00ednicas, obst\u00e9tricas y neonatales de la ces\u00e1rea primaria en mujeres mult\u00edparas",
    "authors": "Santiago Vasco Morales, Carmen Dur\u00e1n Verdesoto, Mar\u00eda Fernanda Morales Carrasco, Mar\u00eda Elena Borja Santin, Paola Toapanta Pinta",
    "journal": "Ginecolog\u00eda y Obstetricia de M\u00e9xico",
    "doi": "https://ginecologiayobstetricia.org.mx/articulo/determinantes-clinicas-obstetricas-y-neonatales-de-la-cesarea-primaria-en-mujeres-multiparas",
    "enfoque": "Analiza m\u00faltiples factores de riesgo cl\u00ednicos, obst\u00e9tricos y neonatales como edad materna y macrosom\u00eda fetal para comprender las indicaciones de realizar una ces\u00e1rea primaria en mujeres que ya han tenido partos m\u00faltiples.",
    "importancia": "Las tasas de ces\u00e1rea se mantienen altas en varias regiones; definir determinantes permite desarrollar intervenciones y pol\u00edticas hospitalarias dirigidas a la reducci\u00f3n adecuada de la intervenci\u00f3n quir\u00fargica innecesaria.",
    "category": "Obstetricia",
    "icon": "pregnant_woman",
    "img": "data:image/webp;base64,UklGRswBAABXRUJQVlA4IMABAACwEACdASpQAFAAP3GuzV60rakmqPbaqpAuCUAYQQ1UAgYifp/sbw8zRy0ZT9h1DvhHUV+GfxnNk99CPKM3udJVhuWt+9lf9SD1zUL3W+FvXQ1MVQjuuig5GvyzHSNwq3ZXyR30Wm0VDT1ffDzErxiwuWo+EkuVJmLkqOedV+CizkFBX/QxqvnM1aSE/RAAAP7vteID5Y9oVy+QXkNY3ET1MMSdL+KtzjAroPvtGf1m0ReNFDbcbTZBNGiNd+y6jp/qdLDFYRSx6ZE7S1xcsZO2QJPy8gtewFfMeFsCQFsMt0NHqujhf3znk7MgSS2y9GsTSeh46fCUDqO+dVUBhPGM+0GweQazQpNtozBUFTQhRAb6h7QZ15AXnU82wNQUH9FOs3GWTbySzUjeQEW1MXhH4Y4h9p25Rbek3WNKyLvEfMA2HeYJCABtOL317RhGqBMY16SUBtO8JDz96Hfp99/F4G8y6IRfgRHIXEyt0bEBKpnb5rotzyaURivogg6a12rvTJRtotf/MGv0aXAPt2x5fKKVBtUgYx8h9ZPkAngVOBmMZxtIoHcoBHn7mUg75eWA/3Lmx2qYpQpr0Ps25wAA"
},
{
    "id": "pdc-lactancia-exclusiva",
    "title": "Factores maternos y neonatales asociados a la lactancia materna exclusiva al egreso hospitalario",
    "authors": "Paola Cristina Toapanta-Pinta, Adriana Paola Sinchiguano C\u00f3ndor, Deicy Maribel Muso Defaz, Ang\u00e9lica Oliva Gualavis\u00ed Landeta, Blanca Llilman Parra Cadena, Santiago Vasco-Morales",
    "journal": "Enfermagem e Texto",
    "doi": "https://pmc.ncbi.nlm.nih.gov/articles/PMC12707856/",
    "enfoque": "Investigaci\u00f3n en m\u00e1s de 22,000 registros hospitalarios usando modelos de regresi\u00f3n log\u00edstica que resalta una alta tasa (91.55%) de lactancia materna exclusiva, pero identifica determinantes negativos como parto por ces\u00e1rea y bajo peso al nacer.",
    "importancia": "Sirve para promover estrategias y pol\u00edticas p\u00fablicas de lactancia dentro del \u00e1mbito cl\u00ednico-hospitalario desde la hora cero tras el nacimiento, priorizando a madres de ces\u00e1reas para reducir las barreras.",
    "category": "Neonatolog\u00eda",
    "icon": "child_care",
    "img": "data:image/webp;base64,UklGRhACAABXRUJQVlA4IAQCAABwEACdASpQAFAAP3GkyF40qqemrNgJEpAuCWMAyjxpDXodZHYdT7ea1eHgPI70fLZf3YJ+2QDX2jJnmIQmnImU0CPmjsS4DvnwIvLbAfb7tuer9vjJwjssbOhQhfoPNjxlnVMPMWGcUrSIxeI3aRP8MjlT02m+GPCnaIki37Fo/7jxnbeDeQtv+K3TAAD+8dBTekF+pK5W0iXeo8Sa7O28XsUZwzfhq8rHOWTXU/OLk6XObfxaDR74RdlN8A5htIHdyjITYD15nz3vAQxf0b3LAdUGzHW5z8wOs/F8y67Y/g8FhRaa4Hwcbl+u2ALRXvReyZXDvri4fSq7ln3ZgDCPbuIq2CvVr1giji3RBb/iff1ssanN1NIdEawBIyNpyppKGdcKsezI6u7ojyZX9+hjJLpPKk9uC9og6S3WFWGqHmMDwLIhFhrAj79z04azn0RsR6gJGuwyDeWSV3KYHNt+ZsO9WehaO8J8iL58Lb9KmUWjIj6FeRBtd3X264hl1RDkYOXyE5RnN5hWQ2DHKe5XlgCJohP73TcrdlFWp7LNLq491RYdOHrQR1ZIFt7LVQOtF3OYF1XbJ+4RxrYmuTgMXgb5fJIUNg0EvRmqx0DizNmb0RFb5JrEzGpifnjf8nMgVfL7pvEnIVL9fHQwT82eIWbce4T0q7ZKRdCsBS/m4jawAAA="
},
{
    "id": "pdc-gastrosquisis",
    "title": "Prevalencia y factores de mortalidad en la hospitalizaci\u00f3n inicial por gastrosquisis",
    "authors": "Santiago Vasco-Morales, Christian Vega-Reyes, Antonio Cer\u00f3n-Caicedo, Nicole Orozco-S\u00e1nchez, Cristhian Vasco-Toapanta, Paola Cristina Toapanta-Pinta",
    "journal": "Andes Pediatrica",
    "doi": "https://doi.org/10.32641/andespediatr.v96i4.5517",
    "enfoque": "Estudio sobre 175 neonatos con gastrosquisis, identificando asociaci\u00f3n de complicaciones m\u00faltiples, puntuaciones bajas de Apgar y bajo peso al nacer con un incremento estad\u00edstico en el riesgo cl\u00ednico de desenlace fatal.",
    "importancia": "Subraya la urgencia de enfoques m\u00e9dicos multidisciplinarios avanzados e intervenciones tempranas para las anomal\u00edas cong\u00e9nitas de pared abdominal en la unidad de terapia intensiva neonatal para aumentar la supervivencia.",
    "category": "Neonatolog\u00eda",
    "icon": "child_care",
    "img": "data:image/webp;base64,UklGRtQBAABXRUJQVlA4IMgBAADwDwCdASpQAFAAP3Gox1u0rKgkK5Od+pAuCU0sq6lXCkRkKkuKBIiSrJIpC8ZvThVy7B9UQEXonzDKFzimbA5JqqZdfm3Uh4TCOODORVomCKRfNH8gF8b5c+DygEFGeN/zAE3PSd85sm2tQrT3C7mffYzli+YGReLpE11028g6YupTUtGNwFYAAP70y51YOAypQijxQUkgIV4nqlhzX12KEYNW+9fzgZxu1UNxa2HgwZyOFsyoq9fAQlxyx0NRRG2Fy+gTqyH5vnUdu3JM4Zgboj/5tdi0BZqfk82SHn6vrTHIItHOJE3t4xtD8mA6uHO4W5UI/lHVBIR57jny8Z+r5ymg6YnRAXQbqFQrGXoBSWkbHYTfcNMF/kbIpOXEompaa41jHk9+/LyS6AjldUOfLxA7Eqvd2NnGuCFQNmMt4VPu4JG5GjZCS61A+IfSdKzoyxskbZLMTrGfQzFxN729O789wyKz81DIbc/8s99QrIX13A+fwGhLQ0dm5e9GgyJXiA59qJqT1EbCsywuNlAuq123BYh0uLB+JX9cgoVyz2svFpcpIGN0v8dgmldcht9NasCYiJyn86/jCDjBinbcsKIeTlWAAAA="
},
{
    "id": "pdc-dermatitis-neurologica",
    "title": "Neurological disorders in infants may represent a potential risk factor for the development of atopic dermatitis",
    "authors": "Santiago Vasco-Morales",
    "journal": "Revista de Medicina de Ribeir\u00e3o Preto",
    "doi": "https://revistas.usp.br/rmrp/es/article/view/230186",
    "enfoque": "Explora y expone de qu\u00e9 manera des\u00f3rdenes sist\u00e9micos neurol\u00f3gicos pueden representar factores de alto riesgo predisponentes para el eventual desarrollo de dermatitis at\u00f3pica e incremento agudo de inmunoglobulina E (IgE).",
    "importancia": "Ofrece perspectivas novedosas orientadas al an\u00e1lisis integrativo entre la neurolog\u00eda pedi\u00e1trica y la inmunolog\u00eda-dermatolog\u00eda, promoviendo detecci\u00f3n de alertas cl\u00ednicas tempranas y un abordaje hol\u00edstico.",
    "category": "Neonatolog\u00eda",
    "icon": "child_care",
    "img": "data:image/webp;base64,UklGRuYBAABXRUJQVlA4INoBAAAQDgCdASpQAFAAP2mcwlizqycjsfW+inAtCUAaEgzxFD2M98YmcRRZMd3euRlRef8wzFNivuGPNF7pu06Cw6XmzJOr1a7eQ+tLjFKd3qdbHasFDOCsn8eaDP9AVTHxXvUKOIRbZGh77rA5JOPoNaU6X1nRdT1zB9AAAP7tSSD17PB7337iZ8AiWV5Lttpr6NFiiZox0xuYHJ8UjdScFZkzBckXQGJYqtnqLqtcn1KYmEGcfPr92/W8OoYtsaWQ77u6INTQWE3Bj3gg3D4zd7DrdGZRHpNiSoJOWI0Dq7CDVi3u6ANZEmekSpsteoL2JL4LYAsUpaPc7WVd/NxDSM2Bif1k5V9kB7xnP1SNas6yz+O+iTL/yOIrTXvFduixLDoowjSWCFNQ/wNsyL2AdGG9HplMtZgjXfDv/RIW3bmGsNLziJwhbsaIS1Mm5uOBRAMwWv9HOoNfj36U06i/sIm8gGOOmrUPPVDZhJDuz+/1sNDm62Gk2ZoY/TdJP0Ob3F6i6UXpBIVAJPL3g4oLTM+svPmdW2wzODDJeeZFs1P/0gjcSNc1Wzha105xeodHZteyouuVLeNVWBwyFQmX2zv39xnRg6wkmFYGw7j+4NXYTjlUkcbUMc5sAAA="
}
]

html_template = """<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="utf-8"/>
    <meta content="width=device-width, initial-scale=1.0" name="viewport"/>
    <title>Publicaciones Científicas</title>
    <script id="tailwind-config">
        tailwind.config = {{
            darkMode: "class",
            theme: {{
                extend: {{
                    colors: {{
                        "primary": "#1d4fd7",
                        "background-light": "#f6f6f8",
                        "background-dark": "#111521",
                    }},
                    fontFamily: {{
                        "display": ["Work Sans", "sans-serif"]
                    }},
                    borderRadius: {{"DEFAULT": "0.25rem", "lg": "0.5rem", "xl": "0.75rem", "full": "9999px"}},
                }},
            }},
        }}
    </script>
    <script src="https://cdn.tailwindcss.com?plugins=forms,container-queries"></script>
    <link href="https://fonts.googleapis.com/css2?family=Work+Sans:wght@300;400;500;600;700;800;900&display=swap" rel="stylesheet"/>
    <link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght@100..700,0..1&display=swap" rel="stylesheet"/>
    <link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght,FILL@100..700,0..1&display=swap" rel="stylesheet"/>
    <style>
        .material-symbols-outlined {{
            font-variation-settings: 'FILL' 0, 'wght' 400, 'GRAD' 0, 'opsz' 24;
        }}
        .scrollbar-hide::-webkit-scrollbar {{
            display: none;
        }}
        .scrollbar-hide {{
            -ms-overflow-style: none;
            scrollbar-width: none;
        }}
    </style>
</head>
<body class="bg-background-light dark:bg-background-dark font-display text-slate-900 dark:text-slate-100">
<div class="relative flex h-auto min-h-screen w-full flex-col group/design-root overflow-x-hidden">
    <div class="layout-container flex h-full grow flex-col">
        <!-- Header / Navigation -->
        <header class="flex items-center justify-between whitespace-nowrap border-b border-solid border-slate-200 dark:border-slate-800 bg-white dark:bg-slate-900 px-6 lg:px-20 py-4 sticky top-0 z-40">
            <div class="flex items-center gap-8">
                <div class="flex items-center gap-3 text-primary">
                    <span class="material-symbols-outlined text-3xl">school</span>
                    <h2 class="text-slate-900 dark:text-white text-xl font-bold leading-tight tracking-tight">Publicaciones</h2>
                </div>
            </div>
            <div class="flex flex-1 justify-end gap-8">
                <a href="index.html" class="flex items-center justify-center gap-2 px-4 py-2 bg-slate-100 dark:bg-slate-800 text-slate-700 dark:text-slate-300 rounded-lg font-medium hover:bg-slate-200 dark:hover:bg-slate-700 transition-all">
                    <span class="material-symbols-outlined">arrow_back</span>
                    Volver al Menú Principal
                </a>
            </div>
        </header>

        <!-- Hero Section -->
        <div class="w-full">
            <div class="relative flex min-h-[450px] flex-col gap-6 bg-cover bg-center bg-no-repeat items-center justify-center px-4 py-20" data-alt="Professional medical research" style='background-image: linear-gradient(rgba(17, 21, 33, 0.75), rgba(17, 21, 33, 0.85)), url("https://lh3.googleusercontent.com/aida-public/AB6AXuCbYOx3rZ8xw_kufDvFO7LJd2Y5gR7iedwcXY9y2vh6oyIHnU9xcvbA2tCCQdfBQeoiZLd_Lz_FuIiQPXY6NkXzJlxEWe_u-WrcoEBRNdrQhscBhK4fc8xDKgCkKsgqfufWA0NiVsFICy42IKKyemuLCnbl21fcDv-lNYO38Cful9B2gOoc6ZHB7SwBTgYnScLylDMI4TLz_-zO4PDoCISpozkZDlZUX9l9nB5-SbKrZAheWVuqs8nBDWJiHQytKKdNufxys-1g5WM");'>
                <div class="flex flex-col gap-4 text-center max-w-3xl">
                    <h1 class="text-white text-4xl md:text-6xl font-black leading-tight tracking-tight">
                        Publicaciones Científicas
                    </h1>
                    <p class="text-slate-200 text-lg md:text-xl font-normal leading-relaxed">
                        Acceda a las últimas investigaciones en Neonatología, Obstetricia y Educación Médica con el más alto rigor académico.
                    </p>
                </div>
                <!-- Hero Search Bar -->
                <div class="w-full max-w-2xl mt-4">
                    <div class="flex w-full items-stretch rounded-xl overflow-hidden shadow-2xl bg-white dark:bg-slate-800 p-1.5 focus-within:ring-2 focus-within:ring-primary/50 transition-all">
                        <div class="text-slate-400 flex items-center justify-center pl-4">
                            <span class="material-symbols-outlined">search</span>
                        </div>
                        <input id="pdc-searchBar" class="w-full border-none bg-transparent focus:ring-0 text-slate-900 dark:text-white placeholder:text-slate-400 px-4 text-base outline-none" placeholder="Buscar por título, autor o palabra clave..."/>
                    </div>
                </div>
            </div>
        </div>

        <!-- Main Content -->
        <main class="max-w-7xl mx-auto w-full px-6 py-12">
            <!-- Category Filters -->
            <div class="flex items-center gap-3 mb-10 overflow-x-auto pb-2 scrollbar-hide" id="category-filters">
                <button class="filter-btn active flex h-10 shrink-0 items-center justify-center gap-2 rounded-full bg-primary text-white px-6 text-sm font-semibold shadow-md transition-all" data-filter="all">
                    <span class="material-symbols-outlined text-sm">grid_view</span>
                    Todos
                </button>
                <button class="filter-btn flex h-10 shrink-0 items-center justify-center gap-2 rounded-full bg-white dark:bg-slate-800 border border-slate-200 dark:border-slate-700 text-slate-700 dark:text-slate-300 px-6 text-sm font-medium hover:border-primary/50 transition-all" data-filter="Neonatología">
                    <span class="material-symbols-outlined text-sm">child_care</span>
                    Neonatología
                </button>
                <button class="filter-btn flex h-10 shrink-0 items-center justify-center gap-2 rounded-full bg-white dark:bg-slate-800 border border-slate-200 dark:border-slate-700 text-slate-700 dark:text-slate-300 px-6 text-sm font-medium hover:border-primary/50 transition-all" data-filter="Obstetricia">
                    <span class="material-symbols-outlined text-sm">pregnant_woman</span>
                    Obstetricia
                </button>
                <button class="filter-btn flex h-10 shrink-0 items-center justify-center gap-2 rounded-full bg-white dark:bg-slate-800 border border-slate-200 dark:border-slate-700 text-slate-700 dark:text-slate-300 px-6 text-sm font-medium hover:border-primary/50 transition-all" data-filter="Educación Médica">
                    <span class="material-symbols-outlined text-sm">school</span>
                    Educación Médica
                </button>
            </div>

            <!-- Publications Grid -->
            <div id="pdc-publications" class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
                {cards}
            </div>
        </main>


    </div>
</div>

<!-- Detailed View Overlay Modal (Hidden by default) -->
<div id="detail-modal" class="fixed inset-0 z-50 bg-slate-900/80 backdrop-blur-sm hidden justify-center items-start overflow-y-auto pt-10 pb-10 opacity-0 transition-opacity duration-300">
    <div class="relative w-full max-w-[960px] bg-background-light dark:bg-slate-900 rounded-xl shadow-2xl overflow-hidden mb-10 mx-4 transform scale-95 transition-transform duration-300 mx-auto" id="detail-modal-content">
        <!-- Close Button -->
        <button id="close-modal" class="absolute top-4 right-4 z-50 bg-black/40 hover:bg-black/60 backdrop-blur-md text-white rounded-full p-2.5 transition-colors shadow-lg">
            <span class="material-symbols-outlined">close</span>
        </button>
        
        <!-- Hero Image Section -->
        <div class="relative min-h-[350px] w-full bg-slate-800 shadow-inner">
            <div id="modal-img" class="absolute inset-0 bg-cover bg-center" style='background-image: linear-gradient(0deg, rgba(17, 21, 33, 0.9) 0%, rgba(17, 21, 33, 0) 70%), url("");'></div>
            <div class="absolute bottom-0 left-0 p-8 w-full z-10">
                <div class="flex flex-wrap gap-2 mb-4">
                    <span id="modal-category" class="px-3 py-1 bg-primary text-white text-xs font-bold rounded-full uppercase tracking-wider shadow-sm">Categoría</span>
                </div>
                <h1 id="modal-title" class="text-white text-3xl md:text-4xl font-black leading-tight tracking-tight max-w-4xl drop-shadow-md">Título del Artículo</h1>
            </div>
        </div>

        <!-- Content Area -->
        <div class="p-6 md:p-8 space-y-8">
            <!-- Metadata Row -->
            <div class="flex flex-col md:flex-row justify-between items-start md:items-center gap-6 border-b border-slate-200 dark:border-slate-700 pb-8">
                <div class="flex flex-col gap-3">
                    <p class="text-slate-700 dark:text-slate-300 text-base font-medium flex items-center gap-2">
                        <span class="material-symbols-outlined text-primary text-sm">menu_book</span>
                        Publicado en <span id="modal-journal" class="text-yellow-500 dark:text-yellow-400 font-bold">Revista</span>
                    </p>
                    <p class="text-yellow-500 dark:text-yellow-400 font-semibold text-sm flex items-start gap-2 max-w-2xl">
                        <span class="material-symbols-outlined text-yellow-500 dark:text-yellow-400 text-sm mt-0.5">person</span>
                        <span id="modal-authors">Autores</span>
                    </p>
                    <div class="flex items-center gap-2 text-yellow-500 dark:text-yellow-400 text-sm font-medium mt-1">
                        <span class="font-bold">Descarga el artículo: </span>
                        <a id="modal-doi" class="hover:underline break-all" href="#" target="_blank">DOI link</a>
                    </div>
                </div>
            </div>

            <!-- Structured Content Cards -->
            <div class="grid grid-cols-1 md:grid-cols-2 gap-6 pb-4">
                <!-- Section 1 -->
                <div class="bg-white dark:bg-slate-800 p-6 md:p-8 rounded-xl shadow-sm border border-slate-100 dark:border-slate-700">
                    <div class="flex items-center gap-3 mb-5">
                        <div class="bg-primary/10 p-2.5 rounded-lg text-primary">
                            <span class="material-symbols-outlined">clinical_notes</span>
                        </div>
                        <h3 class="text-xl font-bold text-slate-900 dark:text-white">¿Cuál es su enfoque?</h3>
                    </div>
                    <p id="modal-enfoque" class="text-slate-600 dark:text-slate-300 leading-relaxed text-[15px] text-justify">
                        Enfoque texto.
                    </p>
                </div>
                
                <!-- Section 2 -->
                <div class="bg-white dark:bg-slate-800 p-6 md:p-8 rounded-xl shadow-sm border border-slate-100 dark:border-slate-700">
                    <div class="flex items-center gap-3 mb-5">
                        <div class="bg-primary/10 p-2.5 rounded-lg text-primary">
                            <span class="material-symbols-outlined">star</span>
                        </div>
                        <h3 class="text-xl font-bold text-slate-900 dark:text-white">¿Por qué es relevante?</h3>
                    </div>
                    <p id="modal-importancia" class="text-slate-600 dark:text-slate-300 leading-relaxed text-[15px] text-justify">
                        Importancia texto.
                    </p>
                </div>
            </div>
        </div>
    </div>
</div>

<script>
    // Data injection for JS logic
    const articlesData = {json_data};

    document.addEventListener('DOMContentLoaded', () => {{
        const searchBar = document.getElementById('pdc-searchBar');
        const cards = document.querySelectorAll('.pdc-publication');
        const filterBtns = document.querySelectorAll('.filter-btn');
        
        const modal = document.getElementById('detail-modal');
        const modalContent = document.getElementById('detail-modal-content');
        const closeBtn = document.getElementById('close-modal');
        
        let currentFilter = 'all';

        // Filter Logic (Search + Categories)
        function filterArticles() {{
            const query = searchBar.value.trim().toLowerCase();
            
            cards.forEach(card => {{
                const text = card.textContent.toLowerCase();
                const category = card.getAttribute('data-category');
                const matchesSearch = text.includes(query);
                const matchesCategory = currentFilter === 'all' || category === currentFilter;
                
                if (matchesSearch && matchesCategory) {{
                    card.style.display = '';
                }} else {{
                    card.style.display = 'none';
                }}
            }});
        }}

        if (searchBar) {{
            searchBar.addEventListener('input', filterArticles);
        }}

        // Category Buttons
        filterBtns.forEach(btn => {{
            btn.addEventListener('click', () => {{
                // Update active state classes
                filterBtns.forEach(b => {{
                    b.classList.remove('bg-primary', 'text-white', 'shadow-md');
                    b.classList.add('bg-white', 'text-slate-700', 'hover:border-primary/50');
                }});
                
                btn.classList.remove('bg-white', 'text-slate-700', 'hover:border-primary/50');
                btn.classList.add('bg-primary', 'text-white', 'shadow-md');
                
                currentFilter = btn.getAttribute('data-filter');
                filterArticles();
            }});
        }});

        // Open Modal Logic
        cards.forEach(card => {{
            card.addEventListener('click', () => {{
                const targetId = card.getAttribute('data-target');
                const data = articlesData.find(a => a.id === targetId);
                
                if(data) {{
                    document.getElementById('modal-title').textContent = data.title;
                    document.getElementById('modal-authors').textContent = data.authors;
                    document.getElementById('modal-journal').textContent = data.journal;
                    document.getElementById('modal-category').textContent = data.category;
                    
                    const doiLink = document.getElementById('modal-doi');
                    doiLink.textContent = data.doi;
                    if(data.doi.startsWith('http')) {{
                       doiLink.href = data.doi;
                    }} else {{
                       doiLink.href = '#';
                    }}
                    
                    document.getElementById('modal-enfoque').textContent = data.enfoque;
                    document.getElementById('modal-importancia').textContent = data.importancia;
                    
                    document.getElementById('modal-img').style.backgroundImage = `linear-gradient(0deg, rgba(17, 21, 33, 0.9) 0%, rgba(17, 21, 33, 0) 70%), url("${{data.img}}")`;
                    
                    // Show modal with animation
                    modal.classList.remove('hidden');
                    modal.classList.add('flex');
                    // Small delay to allow display flex to apply before opacity transition
                    setTimeout(() => {{
                        modal.classList.remove('opacity-0');
                        modalContent.classList.remove('scale-95');
                        modalContent.classList.add('scale-100');
                    }}, 10);
                    
                    document.body.style.overflow = 'hidden'; // Prevent background scrolling
                }}
            }});
        }});

        // Close Modal Logic
        function closeModal() {{
            modal.classList.add('opacity-0');
            modalContent.classList.add('scale-95');
            modalContent.classList.remove('scale-100');
            
            setTimeout(() => {{
                modal.classList.add('hidden');
                modal.classList.remove('flex');
                document.body.style.overflow = '';
            }}, 300);
        }}

        closeBtn.addEventListener('click', closeModal);
        modal.addEventListener('click', (e) => {{
            if(e.target === modal) closeModal();
        }});
        
        document.addEventListener('keydown', (e) => {{
            if(e.key === 'Escape' && !modal.classList.contains('hidden')) closeModal();
        }});

        // Legacy function mapping if needed
        window.agregarArticuloSimple = function(datos) {{
            // Custom simplified addition logic can be implemented here if required
            console.log("Adding dynamic article not fully supported with new template yet.", datos);
        }};
    }});
</script>
</body>
</html>
"""

# Actualizar rutas de imágenes a alta resolución si existen localmente
for a in articles:
    hd_path = f"imagenes_png_alta_resolucion/{a['id']}.png"
    if os.path.exists(os.path.join('/home/santiago/MEGA/ANTIGRAVITY/PAGINA WEB', hd_path)):
        a['img'] = hd_path
        print(f"Usando imagen HD para: {a['id']}")

cards_html = ""
for a in articles:
    cards_html += f"""
                <article class="pdc-publication bg-white dark:bg-slate-900 rounded-xl overflow-hidden shadow-sm hover:shadow-xl transition-all duration-300 border border-slate-100 dark:border-slate-800 flex flex-col group cursor-pointer hover:-translate-y-1" data-target="{a['id']}" data-category="{a['category']}">
                    <div class="h-52 w-full overflow-hidden relative shrink-0">
                        <img src="{a['img']}" alt="{a['title']}" class="w-full h-full object-cover transition-transform duration-500 group-hover:scale-105" />
                        <div class="absolute inset-0 bg-black/5 group-hover:bg-transparent transition-all pointer-events-none"></div>
                    </div>
                    <div class="p-6 flex flex-col grow">
                        <span class="inline-block px-3 py-1 bg-primary/10 text-primary text-xs font-bold rounded-full mb-3 uppercase tracking-wider w-max">{a['category']}</span>
                        <h3 class="text-lg md:text-xl font-bold leading-snug mb-3 group-hover:text-primary transition-colors line-clamp-3" title="{a['title']}">{a['title']}</h3>
                        <div class="mt-auto pt-4 flex items-start gap-2 text-yellow-500 dark:text-yellow-400 font-semibold border-t border-slate-100 dark:border-slate-800">
                            <span class="material-symbols-outlined text-sm shrink-0 mt-0.5">person</span>
                            <span class="text-sm font-medium line-clamp-2" title="{a['authors']}">{a['authors']}</span>
                        </div>
                    </div>
                </article>
    """

final_html = html_template.format(
    json_data=json.dumps(articles),
    cards=cards_html
)

# Guardar en todos los archivos necesarios
output_files = [
    '/home/santiago/MEGA/ANTIGRAVITY/PAGINA WEB/publicaciones.html',
    '/home/santiago/MEGA/ANTIGRAVITY/PAGINA WEB/index.html',
    '/home/santiago/MEGA/ANTIGRAVITY/PAGINA WEB/publicaciones_github.html'
]

for filepath in output_files:
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(final_html)
    print(f'Archivo generado: {filepath}')
