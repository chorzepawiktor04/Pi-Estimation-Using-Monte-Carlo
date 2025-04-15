import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches


def calc_inside(x,y):                          #funkcja obliczająca estymację liczby pi zgodnie ze wzorem
    points_inside = x**2 + y**2 < 1
    inside_count=0
    for i in points_inside:
        if i == 1:
            inside_count+=1       
    pi_estimate = 4*inside_count/points
    return pi_estimate, points_inside

probki_all = []
pi_estimates_all = []
for k in range(1,11):                           #10 serii obliczeń dla każdej ilości punktów
    probki = []
    pi_estimates = []
    for i in range(1,7):                        #przedzial od 10 do 1 000 000 -> wykorzystanie prawa wielkich liczb
        points = 10**i
        probki.append(points)
        x = np.random.uniform(0, 1, points)     #punkty są za każdym razem losowane zgodnie z random distribution -> element "losowości" na którym oparte jest Monte Carlo i inne metody probabilistyczne
        y = np.random.uniform(0, 1, points)

        pi_estimate, points_inside = calc_inside(x, y)
        pi_estimates.append(pi_estimate)

        if k==1:                                                        #wizualizację rozkładu punktów wewnątrz i na zewnątrz fragmentu okręgu pokazuje tylko dla pierwszej serii aby zachować przejrzystość przy outpucie

            fig, ax = plt.subplots()
            arch = patches.Circle((0,0),1, edgecolor='red', facecolor='none')
            ax.add_patch(arch)
            ax.scatter(x, y, color='green', s=1) 
            ax.scatter(x[points_inside], y[points_inside], color = 'red', s=1)
            plt.xlim(0, 1)
            plt.ylim(0, 1)
            plt.show()
            print(pi_estimate)
    probki_all.append(probki)
    pi_estimates_all.append(pi_estimates)

temp = len(probki_all)
colors = ['g','r','b','y','m','k','c','olive','teal','crimson',]
plt.figure()

for j in range(temp):                                                           #wykres pokazujący jak w każdej z serii wyglądała ścieżka dążenia do pi                     
    plt.plot(probki_all[j], pi_estimates_all[j], marker='o', linestyle='-', color=colors[j])

plt.axhline(y=np.pi, color='r', linestyle='--', label='π = 3.1416')
plt.xscale('log')
plt.xlabel('Liczba losowań (N)')
plt.ylabel('Estymowana wartość π')
plt.title('Ścieżki dążenia do π')
plt.legend()
plt.show()

plt.figure(figsize=(12, 12))

for i, N in enumerate(probki_all):                                           #histogram pokazujący jak wraz ze wzrostem liczby próbek zbliżamy się do wartości 3.14(najbardziej widać to po zmieniającej się skali na każdym wykresie)                             
    plt.subplot(3, 2, i+1) 
    plt.hist([pi_estimates_all[j][i] for j in range(10)], bins=5, alpha=0.7, color='blue', edgecolor='black')
    plt.axvline(x=np.pi, color='r', linestyle='--', label='π = 3.1416')
    plt.xlabel('Estymowana wartość π')
    plt.ylabel('Liczba wystąpień')
    plt.legend()

#plt.tight_layout()  
plt.show()


#Za pomocą Metody Monte Carlo udało się pokazać(używając bardzo podstawowych narzędzi) jaki wpływ na jakość estymacji ma zwiększanie liczby próbek
#Zarówno wykres pokazujący ściężkę dążenia do pi jak i histogram jasno pokazują, że jest to efektywny sposób symulowania takich estymacji - chociaż nie jest on perfekcyjny
#W fazie testowania, kilka razy zdarzyło się że przybliżenie dla 10^5 próbek było bardzo zbliżone, a czasem nawet lepsze niż to dla 10^6, co na pierwszy rzut oka kłóci się z naszą tezą
#Jest to jednak po prostu ukazanie limitacji metody Monte Carlo, która w ostatecznym rozrachunku jest jedynie przybliżeniem i pomimo tego że możemy operować na dużych liczbach(jeśli chodzi o liczbę próbek) to jednak nigdy nie zbliżymy się do nieskończoności, czyli do punktu w którym wyniki powinny być idealne(zawsze zgodne z teorią)
#Ostatecznie uważam, że dzięki metodzie Monte Carlo można było w bardzo przystępny sposób wykonać tę ciekawą(choć może trywialną) estymację, a wizualizacja wyników potwierdziła trafność doboru metody do problemu.
    
    
   