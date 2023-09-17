## Inspiration
Manually creating calendar events sucks. Especially for weird events. You might teach an evening class on Wednesdays and Thursdays. Or maybe you have to meet with a colleague 3 times a week during work hours, but not on Mondays or Fridays! All this complexity can be a nightmare to work with. Sometimes, we even think there’s so much going on that we have no time to spare at all. We wanted a solution, so we created CalPal, an AI-powered smart calendar that automates all your time management needs with generative AI.

## What it does
Introducing **CalPal - Your Personal Smart Calendar**. Tired of the endless back-and-forth of scheduling? Let CalPal revolutionize your routine! With just a simple prompt, watch as AI effortlessly crafts your perfect schedule, complete with a beautiful calendar interface. You can enter a short phrase or a complex passage and the AI will populate your calendar with all the relevant events. Plus, enjoy all the classic calendar features seamlessly integrated. Say goodbye to the hassle of manual event planning and hello to a smarter, more efficient way to manage your time. Let CalPal take the reins, so you can focus on what truly matters.

## How we built it
We began by brainstorming some common problems we all experience and landed on the idea of CalPal after talking about our busy school terms. Once we had our idea, we started making the early conceptualizations on Figma and created our name and logo. Our frontend is built with React and uses the npm package react-big-calendar to build a sleek interactive calendar interface.
Our application is full-stack, with a backend built with flask, and components linked together via API endpoints.

The backend leverages Cohere’s generative API to create a tailored schedule from a prompt. The AI’s response is parsed to gather data for each event (including details like the title, start date/time, and end date/time). Previously scheduled events are also parameters to ensure there are no conflicts. We store these events in our PostgreSQL database, powered by CockroachDB. 

## Challenges we ran into
This was the first in-person hackathon for most of our team! None of us are front-end developers, so building the React website was tricky to learn. Some team members had CockroachDB connection issues due to their environment setups, which resulted in the DB taking a long time to set up. 

Another challenge we faced was parsing the AI’s response for date-times and relevant information since the response is non-deterministic. The occasionally wacky responses meant that we needed to build a robust backend to handle all edge cases that the AI might produce. 

## Accomplishments that we're proud of
- Created a finished product despite being exhausted for much of the hackathon
- Designed the architecture and followed good practices, even if it took us longer
- Gained experience with the complete stack and built 4 main endpoints along with a frontend
- Learnt and implemented technologies that were completely new to us including React, CockroachDB, and CohereAI 

## What we learned
On top of learning about CockroachDB and Cohere Generative AI, we had to do plenty of end-to-end testing of our product. We debugged each other’s code and wrangled with the AI’s responses. We also powered through many front-end bugs and quirks. Overall, we’re glad we got to learn more about full-stack development.

## What's next for CalPal
The future of CalPal is brimming with exciting possibilities! Here's a glimpse into what's next for this smart calendar:
**1. Collaborative Features**: We can enhance scheduling meetings between two or more CalPals by automatically scheduling meetings when all parties are available, without needing to manually wiggle around the time when something new comes up.
**2. Voice Assistant Integration**: Incorporating a voice assistant into CalPal not only enhances accessibility but also introduces an intuitive way to interact with the calendar. You can verbally instruct CalPal to add events, adjust timings, or even ask for suggestions based on your preferences. 
**3. Seamless Calendar Sync**: Enabling CalPal to sync with popular calendars like Google Calendar and Apple Calendar is a crucial step in ensuring a seamless user experience. This feature will allow users to manage their events across platforms effortlessly.
**4. Enhanced Personalization**: CalPal can further refine AI usage to provide highly personalized suggestions and recommendations for users. This might include insights on time management, productivity tips, and event prioritization based on individual preferences and past behaviors.

