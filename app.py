from flask import Flask, render_template
from FlowerItem import FlowerItem

app = Flask(__name__)

item1 = FlowerItem(1, "Cosmos", "images/flower1.jpg",
                   "Cosmos are annual flowers with colorful, daisy-like flowers that sit atop long, slender stems."
                   "Cosmos species are native to scrub and meadowland in Mexico where most of the species occur, the United States, as far north as the Olympic Peninsula in Washington, Central America, and to South America as far south as Paraguay.", 80)
item2 = FlowerItem(2, "Gardenblue flower", "images/flower2.jpg",
                   "Delphiniums offer some of the truest-blue flowers in the garden. Delphiniums do need full Sun to grow but they prefer cool weather. So let seeds germinate in winter and the plant will bloom in early spring.", 250)
item3 = FlowerItem(3, "Red Anemone", "images/flower3.jpg",
                   "Anemone coronaria, the poppy anemone, Spanish marigold, or windflower, is a species of flowering plant in the buttercup family Ranunculaceae, native to the Mediterranean region."
                   "Anemone coronaria is a herbaceous perennial tuberous plant growing to 20–40 cm tall, rarely to 60 cm (0.75–1.50 feet), spreading to 15–23 cm (0.50 to 0.75 feet), with a basal rosette of a few leaves, the leaves with three leaflets, each leaflet deeply lobed. The flowers which bloom from April to June are borne singly on a tall stem with a whorl of small leaves just below the flower; the flower is 3–8 cm diameter, with 5–8 red (but may be white or blue) showy petal-like tepals and a black centre. The pollen is dry, has an unsculpted exine, is less than 40 nm in diameter, and is usually deposited within 1.5 m of its source. This central mound consists of tightly packed pistils in the centre, with a crown-like ring of stamens surrounding this, which gives the species its name.The flowers produce 200–300 seeds.",
                   200)
item4 = FlowerItem(4, "Marigold", "images/flower4.jpg",
                   "Marigold is a flowering plant in the daisy family Asteraceae. It is probably native to southern Europe, though its long history of cultivation makes its precise origin unknown, and it may possibly be of garden origin. Marigolds germinate quickly, sprouting within a few days and blooming in about 8 weeks, making them easy to grow from seed. French marigolds can easily be started from seed, while African marigolds are best purchased as young plants (when started from seed, they can take a long time to flower).",
                   100)
item5 = FlowerItem(5, "Sun Flower", "images/flower5.jpg",
                   "Sunflowers originate in the Americas. They were first domesticated in what is now Mexico and the Southern United States.Domestic sunflower seeds have been found in Mexico, dating to 2100 BCE. Its scientific name comes from the Greek words helios (“sun”) and anthos (“flower”). The flowers come in many colors (yellow, red, orange, maroon, brown). A fairly fast-growing flower for their size, most sunflower varieties mature in only 80 to 95 days. The largest sunflower varieties grow to over 16 feet in height, while smaller varieties have been developed for small spaces and containers and rarely grow larger than a foot tall! The flower heads can reach over 12 inches in diameter within the large seeded varieties.",400)
item6 = FlowerItem(6, "Orchid", "images/flower7.jpg",
                   "Orchids are easily distinguished from other plants, as they share some very evident derived characteristics or synapomorphies. Among these are: bilateral symmetry of the flower (zygomorphism), many resupinate flowers, a nearly always highly modified petal (labellum), fused stamens and carpels, and extremely small seeds. The greatest concentration of orchid varieties is found in the tropical regions of the world, namely in Asia and Central and South America. In most of North America, orchids must be grown indoors (exceptions include native species such as the lady’s slipper).orchids grown indoors as houseplant typically need quite a lot of light—either in the form of supplemental lighting or by being placed in a location where there is lots of diffused natural light.",
                   400)
flowersgroup1 = [item1, item2, item3]
flowersgroup2 = [item4, item5, item6]


def get_flower_by_id(flower_id):
    for item in flowersgroup1:
        if (str(item.id) == flower_id):
            return item

    for item in flowersgroup2:
        if (str(item.id) == flower_id):
            return item


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/flowers')
def show_flower_images():
    return render_template('flowers.html', first_group_items=flowersgroup1, second_group_items=flowersgroup2)


@app.route('/flowerdetails/<flowerid>')
def show_flower_details(flowerid):
    flower_item = get_flower_by_id(flowerid)
    return render_template('flowerdetails.html', flower_image=flower_item.image_name,
                           flower_info=flower_item.information, flower_price=flower_item.price)


if __name__ == "__main__":
    app.run(debug=True, port=5000)
