#Készíts egy rövid programot, amely a felhasználótól bekéri a kör sugarát, és ennek alapján kiszámolja a kör kerületét és területét!
sugar = int(input("Kérem adjon meg egy számot(sugár/cm): "))
kerulet = sugar*2/3.14
terulet = sugar**2/3.14
print(f"A kör kerülete: {kerulet}cm")
print(f"A kör területe: {terulet}cm")
