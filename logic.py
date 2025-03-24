import aiohttp  # Eşzamansız HTTP istekleri için bir kütüphane
import random
import asyncio
from datetime import timedelta, datetime

import time
class Pokemon:
    pokemons = {}
    # Nesne başlatma (kurucu)
    def __init__(self, pokemon_trainer):
        self.pokemon_trainer = pokemon_trainer
        self.pokemon_number = random.randint(1, 1000)
        self.name = None
        self.hp=random.randint(50,100)
        self.power=random.randint(20,50)
        self.ability = None
        self.last_feed_time=datetime.now()
        if pokemon_trainer not in Pokemon.pokemons:
            Pokemon.pokemons[pokemon_trainer] = self
        else:
            self = Pokemon.pokemons[pokemon_trainer]

    async def get_name(self):
        # PokeAPI aracılığıyla bir pokémonun adını almak için eşzamansız bir yöntem
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'  # İstek için URL API'si
        async with aiohttp.ClientSession() as session:  # Bir HTTP oturumu açma
            async with session.get(url) as response:  # GET isteği gönderme
                if response.status == 200:
                    data = await response.json()  # JSON yanıtının alınması ve kodunun çözülmesi
                    return data['forms'][0]['name']  # Bir Pokémon'un adını döndürme
                else:
                    return "Pokemon"  # İstek başarısız olursa varsayılan adı döndürür
                
    async def get_image(self):
        # PokeAPI aracılığıyla bir pokémonun adını almak için eşzamansız bir yöntem
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'  # İstek için URL API'si
        async with aiohttp.ClientSession() as session:  # Bir HTTP oturumu açma
            async with session.get(url) as response:  # GET isteği gönderme
                if response.status == 200:
                    data = await response.json()  # JSON yanıtının alınması ve kodunun çözülmesi
                    return data['sprites']['front_default']  # Bir Pokémon'un adını döndürme
                else:
                    return "Pokemon"  # İstek başarısız olursa varsayılan adı döndürür
    async def info(self):
        # Pokémon hakkında bilgi döndüren bir metot
        if not self.name:
            self.name = await self.get_name()  # Henüz yüklenmemişse bir adın geri alınması
        return f"Pokémonunuzun ismi: {self.name} \nPokémonunuzun sağlığı {self.hp} \nPokémonunuzun gücü {self.power}"  # Pokémon'un adını içeren dizeyi döndürür

    async def show_img(self):
        # PokeAPI aracılığıyla bir pokémonun adını almak için eşzamansız bir yöntem
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'  # İstek için URL API'si
        async with aiohttp.ClientSession() as session:  # Bir HTTP oturumu açma
            async with session.get(url) as response:  # GET isteği gönderme
                if response.status == 200:
                    data = await response.json()  # JSON yanıtının alınması ve kodunun çözülmesi
                    return data['sprites']['front_default']  # Bir Pokémon'un adını döndürme
                else:
                    return "Pokemon"  # İstek başarısız olursa varsayılan adı döndürür
                
    async def get_ability(self):
        # PokeAPI aracılığıyla bir pokémonun adını almak için eşzamansız bir yöntem
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'  # İstek için URL API'si
        async with aiohttp.ClientSession() as session:  # Bir HTTP oturumu açma
            async with session.get(url) as response:  # GET isteği gönderme
                if response.status == 200:
                    data = await response.json()  # JSON yanıtının alınması ve kodunun çözülmesi
                    return data['abilities'][0]['ability'][0]['name'] # Bir Pokémon'un adını döndürme
                else:
                    return "Pokemon"  # İstek başarısız olursa varsayılan adı döndürür

    async def attack(self,target):
        if isinstance(target, Wizard):  # Enemy'nin bir Wizard veri tipi olduğunu (Büyücü sınıfının bir örneği olduğunu) kontrol etme
            chance = random.randint(1, 5) 
        if chance == 1:
            return "Sihirbaz Pokémon, savaşta bir kalkan kullanıldı!"
        if target.hp>self.power:
            target.hp-=self.power
            return f"{self.pokemon_trainer},{target.pokemon_trainer}'a sardırdı!"
        else:
            target.hp=0
            return f"{self.pokemon_trainer},{target.pokemon_trainer}'ı yendi!"

    async def feed(self, feed_interval=20, hp_increase=10):
        current_time = datetime.now()
        delta_time = timedelta(seconds=feed_interval)
        if (current_time - self.last_feed_time) > delta_time:
            self.hp += hp_increase
            self.last_feed_time = current_time
            return f"Pokémon'un sağlığı geri yüklenir. Mevcut sağlık: {self.hp}"
        else:
            return f"Pokémonunuzu şu zaman besleyebilirsiniz: {current_time+delta_time}"
        

class Wizard(Pokemon):
    async def attack(self, enemy):
        return await super().attack(enemy)
    async def feed(self):
        return await super().feed(feed_interval=10,hp_increase=10)


class Fighter(Pokemon):
    async def attack(self, enemy):
        super_power = random.randint(5, 15)  
        self.power += super_power
        sonuc = await super().attack(enemy)  
        self.power -= super_power
        return sonuc + f"\nDövüşçü Pokémon süper saldırı kullandı. Eklenen güç: {super_power}"
    async def feed(self):
        return await super().feed(feed_interval=20,hp_increase=20)
            
if __name__ == '__main__':
    async def main():

        wizard = Wizard("username1")
        fighter = Fighter("username2")
        pokemon=Pokemon('Ege')
        print(await wizard.info())
        print()
        print(await fighter.info())
        print()
        print(await fighter.attack(wizard))
        print(await wizard.info())
        print(await pokemon.info())
        print("pokemon besleme denemesi")
        print(await pokemon.feed())
        print(await wizard.feed())
        print(await fighter.feed())
        time.sleep(10)
        print("pokemon besleme denemesi")
        print(await pokemon.feed())
        print(await wizard.feed())
        print(await fighter.feed())
        time.sleep(10)
        print("pokemon besleme denemesi")
        print(await pokemon.feed())
        print(await wizard.feed())
        print(await fighter.feed())

    asyncio.run(main())