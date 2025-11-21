from typing import Any
from blog.models import post
from django.core.management.base import BaseCommand
import random


class Command(BaseCommand):
    help = "Populate data for the blog app"

    def handle(self, *args: Any, **options: Any):
        # delete data
        post.objects.all().delete()
                    
        title = [
            "Viyana (Bigg Boss Tamil 9) Wiki, Age, Family, Images",
            "Gana Vinoth (Bigg Boss Tamil 9) Wiki, Age, Family, Images",
            "Tushaar Jayaprakash (Bigg Boss Tamil 9) Wiki, Age, Family, Images",
            "Kamaruddin (Bigg Boss Tamil 9) Wiki, Age, Family, Images",
            "Aurora Sinclair (Bigg Boss Tamil 9) Wiki, Age, Family, Images",
            "VJ Parvathy (Bigg Boss Tamil 9) Wiki, Age, Family, Images",
            "Diwakar aka Watermelon Star (Bigg Boss Tamil 9) Wiki, Age, Family, Images",
            "Apsara CJ (Bigg Boss Tamil 9) Wiki, Age, Family, Images",
        ]

        content = [
            "Viyana,one of the newest faces to enter Bigg Boss Tamil Season 9 Tamil Nadu,has quickly captured public attention with her calm presence, articulate communication, and confident individuality. Known for her elegant demeanor and multifaceted talents, she stands out as a contestant who embodies both substance and charm. With her roots in the modeling and entertainment industries, Viyana represents the new wave of South Indian women who balance ambition, intellect, and authenticity in the public eye.",
            "Gana Vinoth,one of the newest faces to enter Bigg Boss Tamil Season 9 Tamil Nadu,has established himself as a prominent figure in the Tamil music industry as a playback singer, lyricist, and live performer. Known for his distinctive voice and energetic performances, Vinoth has gained recognition not only for his songs in films but also for his independent music ventures. His entry into mainstream Tamil cinema and the digital music scene has allowed him to connect with audiences across generations, making him one of the most talked-about voices in contemporary Tamil music.",
            "Tushaar Jayaprakash,one of the newest faces to enter Bigg Boss Tamil Season 9 Tamil Nadu,known for his distinctive Korean-inspired fashion and engaging content, brings a unique blend of cultural influences to the entertainment industry. While he has not publicly disclosed extensive details about his family, he has mentioned in interviews that his roots trace back to Singapore. This multicultural heritage adds depth to his persona, reflecting a fusion of Tamil and Singaporean influences that resonate in his creative expressions.",
            "Kamaruddin,one of the newest faces to enter Bigg Boss Tamil Season 9 Tamil Nadu,widely known in the Malayalam film circle for his grounded performances and comic timing, has now stepped into a whole new world of the Bigg Boss Tamil Season 9 house. The show, which premiered on October 5, 2025, and this season’s contestant lineup has already caught the audience’s eye for its mix of actors, models, influencers, and emerging talents.",
            "Aurora Sinclair,one of the newest faces to enter Bigg Boss Tamil Season 9 Tamil Nadu, Tamil entertainment industry, known for her work as a model, content creator, and aspiring actress. With her striking screen presence and engaging personality, she has been making waves across social media and digital platforms. Aurora is recognized for her versatility in short films, music albums, and creative projects, steadily building a reputation as one of the most promising young entertainers in the industry.",
            "VJ Parvathy,one of the newest faces to enter Bigg Boss Tamil Season 9 Tamil Nadu,When Bigg Boss Tamil Season 9 kicked off on October 5, 2025, one of the contestants who instantly caught everyone’s attention was VJ Parvathy. Known for her energetic screen presence and quick wit, Parvathy’s entry added a dose of charisma and unpredictability to this year’s line-up. Before stepping into the iconic Bigg Boss house, she had already made her mark as a popular television anchor, model, actress and digital creator in the Tamil entertainment circuit.",
            "Diwakar,one of the newest faces to enter Bigg Boss Tamil Season 9 Tamil Nadu, better known to many as Watermelon Star, is a social media influencer who has built a name for himself through quirky content, humorous skits, and an unmistakable style. His selection as a contestant for Bigg Boss Tamil Season 9, which began on October 5, 2025, introduces him to a larger reality-TV audience. Known for his fun-loving and light-hearted persona, Diwakar is expected to bring laughter, unpredictability, and meme-worthy moments into the Bigg Boss house.",
            "Apsar  CJ,one of the newest faces to enter Bigg Boss Tamil Season 9 Tamil Nadu,not only for her confident personality but also for her journey from modelling ramps in Kerala to one of Tamil television’s biggest reality stages. Hailing from Trivandrum, she represents a new generation of South Indian women who are self-assured, expressive, and determined to make their mark in the entertainment industry. Her entry into the Bigg Boss house has drawn attention for her poise, grounded nature, and the quiet strength she brings into every conversation and task.",
        ]

        img_url = [

            "https://tamilglitz.in/wp-content/uploads/2025/10/Viyana-Bigg-Boss-Tamil-9-Contestant-1-650x813.jpg",
            "https://tamilglitz.in/wp-content/uploads/2025/10/Gana-Vinoth-Bigg-Boss-Tamil-9-Contestant-1-650x650.jpeg",
            "https://tamilglitz.in/wp-content/uploads/2025/10/Tushaar-Jayaprakash-Bigg-Boss-Tamil-9-Contestant-5-650x650.jpg",
            "https://tamilglitz.in/wp-content/uploads/2025/10/Kamaruddin-Bigg-Boss-Tamil-9-Contestant-8-650x741.jpg",
            "https://tamilglitz.in/wp-content/uploads/2025/10/Aurora-Sinclair-Bigg-Boss-Tamil-9-Contestant-8-650x714.jpg",
            "https://tamilglitz.in/wp-content/uploads/2025/10/VJ-Parvathy-Bigg-Boss-Tamil-9-Contestant-5-650x813.jpg",
            "https://akm-img-a-in.tosshub.com/indiatoday/images/story/202510/diwaker-bigg-boss-tamil-9-064234263-1x1.jpg?VersionId=YjPyGHqMTJ5zaOZZhplLFpybAaT5Z1nj",
            "https://tamilglitz.in/wp-content/uploads/2025/10/Apsara-CJ-Bigg-Boss-Tamil-9-Contestant-1-650x859.jpeg",
    
        ]

        for title, content, img_url in zip(title, content, img_url):
            post.objects.create(title=title, content=content, img_url=img_url)
        
        self.stdout.write(self.style.SUCCESS('Successfully created post'))