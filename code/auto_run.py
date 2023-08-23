import openai

# Set your OpenAI API key
openai.api_key = "API_KEY_HERE"

my_file = open('./original_datasets/TURK_Original_Cleaned.txt', 'r')
data = my_file.read()
splitting = data.split("\n")

def auto_run(prompt_start, prompt_end, path):
    for i in range (0, len(splitting)):
        prompt_gen = prompt_start+splitting[i]+prompt_end
        response = openai.Completion.create(
    model="text-davinci-003",
    prompt=prompt_gen,
    temperature=0.7,
    max_tokens=376,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
    )
        #print("Prompt Given " + prompt_gen)
        with open(path, 'a') as f:
            stringthing = response['choices'][0]['text']
            stringthing2 = stringthing.replace("\n\n", "")
            stringthing3 = stringthing2.strip()
            f.write(stringthing3)
            f.write("\n")

    print("Done!")

auto_run("Simplify the following sentences according to the provided SARI score. The SARI score is a measure of how well a sentence is simplified. The higher the SARI score, the better it is simplified.\n\nComplex Sentence:In 1998, Culver ran for Iowa Secretary of State and was victorious.\nSARI Score:61.56\nSimple Sentence:Culver became Iowa’s Secretary of State in 1998.\n--\nComplex Sentence:He was also named 1982 \"Sportsman of the Year\" by Sports Illustrated.\nSARI Score: 61.69\nSimple Sentence:He was Sports Illustrated’s \"Sportsman of the Year\" in 1982 .\n--\nComplex Sentence:She was left behind (explanations for this vary) when the rest of the Nicolenos were moved to the mainland.\nSARI Score:62.15\nSimple Sentence:When the rest of the Nicolenos moved to the mainland, she was left behind. No one knows why.\n--\nComplex Sentence:Frederic Chopin's Opus 57 is a berceuse for solo piano.\nSARI Score:67.50\nSimple Sentence:Frederic Chopin's Opus 57 is a lullaby for piano.\n--\nComplex Sentence:",)