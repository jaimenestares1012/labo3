from flask import Flask, request

from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/')
def inicio():
    return {
	"codRes": "00",
	"data": [
		{
			"2022-11-21": "Precio Online S/ 10.70",
			"_id": "774128",
			"categoria": "frutas-y-verduras",
			"nombre": "Papa Amarilla Extra 1Kg",
			"subcategoria": "verduras",
			"tienda": "www.wong.pe",
			"url": "https://www.wong.pe/papa-amarilla-extra-1kg-774128/p"
		},
		{
			"2022-11-21": "Precio Online S/ 9.68 x kg",
			"_id": "4034",
			"categoria": "frutas-y-verduras",
			"nombre": "Papa Amarilla Tumbay x kg",
			"subcategoria": "verduras",
			"tienda": "www.wong.pe",
			"url": "https://www.wong.pe/papa-amarilla-tumbay-x-kg-4034/p"
		},
		{
			"2022-11-21": "Precio Online S/ 4.95",
			"_id": "774134",
			"categoria": "frutas-y-verduras",
			"nombre": "Papa Amarilla Cocktail Comcen 1kg",
			"subcategoria": "verduras",
			"tienda": "www.wong.pe",
			"url": "https://www.wong.pe/papa-amarilla-cocktail-comcen-1kg-774134/p"
		},
		{
			"2022-11-21": "Precio Online S/ 7.00 x kg",
			"_id": "4190",
			"categoria": "frutas-y-verduras",
			"nombre": "Papa Amarilla Huamantanga x kg",
			"subcategoria": "verduras",
			"tienda": "www.wong.pe",
			"url": "https://www.wong.pe/papa-amarilla-huamantanga-x-kg-4190/p"
		},
		{
			"2022-11-21": "Precio Online S/ 10.08",
			"_id": "774126",
			"categoria": "frutas-y-verduras",
			"nombre": "Papa Amarilla Comcen Procesada 1 kg",
			"subcategoria": "verduras",
			"tienda": "www.wong.pe",
			"url": "https://www.wong.pe/papa-amarilla-comcen-procesada-1-kg-774126/p"
		},
		{
			"2022-11-21": "Precio Online S/ 20.07",
			"_id": "774127",
			"categoria": "frutas-y-verduras",
			"nombre": "Papa Amarilla Tumbay Procesada Comcen 2Kg",
			"subcategoria": "verduras",
			"tienda": "www.wong.pe",
			"url": "https://www.wong.pe/papa-amarilla-tumbay-procesada-comcen-2kg-774127/p"
		},
		{
			"2022-11-21": "Precio Online S/ 4.92 x kg",
			"_id": "158740",
			"categoria": "frutas-y-verduras",
			"nombre": "Papa Amarilla Peruanita Cocktail x kg",
			"subcategoria": "verduras",
			"tienda": "www.wong.pe",
			"url": "https://www.wong.pe/papa-amarilla-peruanita-cocktail-x-kg-158740/p"
		},
		{
			"2022-11-21": "Precio Online S/ 6.90 x kg",
			"_id": "4203",
			"categoria": "frutas-y-verduras",
			"nombre": "Papa Amarilla Peruanita Procesada x kg",
			"subcategoria": "verduras",
			"tienda": "www.wong.pe",
			"url": "https://www.wong.pe/papa-amarilla-peruanita-procesada-x-kg-4203/p"
		},
		{
			"2022-11-21": "Precio Online S/ 8.96 x kg",
			"_id": "4175",
			"categoria": "frutas-y-verduras",
			"nombre": "Papa Amarilla Tumbay Procesada x kg",
			"subcategoria": "verduras",
			"tienda": "www.wong.pe",
			"url": "https://www.wong.pe/papa-amarilla-tumbay-procesada-x-kg-4175/p"
		},
		{
			"2022-11-21": "",
			"_id": "135",
			"categoria": "frutas-y-verduras",
			"nombre": "Papa Amarilla Tumbay Especial Metro x kg",
			"subcategoria": "verduras",
			"tienda": "www.wong.pe",
			"url": "https://www.wong.pe/papa-amarilla-tumbay-especial-metro-x-kg-135/p"
		},
		{
			"2022-11-21": "",
			"_id": "71123",
			"categoria": "frutas-y-verduras",
			"nombre": "Papa Amarilla Tumbay Procesada Metro x kg",
			"subcategoria": "verduras",
			"tienda": "www.wong.pe",
			"url": "https://www.wong.pe/papa-amarilla-tumbay-procesada-metro-x-kg-71123/p"
		},
		{
			"2022-11-21": "Precio Online S/ 7.88 x kg",
			"_id": "107974",
			"categoria": "frutas-y-verduras",
			"nombre": "Papa Amarilla Peruanita Procesada Metro x kg",
			"subcategoria": "verduras",
			"tienda": "www.wong.pe",
			"url": "https://www.wong.pe/papa-amarilla-peruanita-procesada-metro-x-kg-107974/p"
		},
		{
			"2022-11-21": "Precio Online S/ 9.63",
			"_id": "2kg",
			"categoria": "frutas-y-verduras",
			"nombre": "Papa Amarilla Tumbay Procesada Agro Selecto 2Kg",
			"subcategoria": "verduras",
			"tienda": "www.wong.pe",
			"url": "https://www.wong.pe/papa-canchan-procesada-agro-selecto-2kg/p"
		},
		{
			"2022-11-21": "Precio Online S/ 7.16 x kg",
			"_id": "4036",
			"categoria": "frutas-y-verduras",
			"nombre": "Papa Huayro x kg",
			"subcategoria": "verduras",
			"tienda": "www.wong.pe",
			"url": "https://www.wong.pe/papa-huayro-x-kg-4036/p"
		},
		{
			"2022-11-21": "",
			"_id": "134",
			"categoria": "frutas-y-verduras",
			"nombre": "Papa Huayro Metro x kg",
			"subcategoria": "verduras",
			"tienda": "www.wong.pe",
			"url": "https://www.wong.pe/papa-huayro-metro-x-kg-134/p"
		},
		{
			"2022-11-21": "Precio Online S/ 8.46",
			"_id": "774132",
			"categoria": "frutas-y-verduras",
			"nombre": "Papa Negra Comcen 2 kg",
			"subcategoria": "verduras",
			"tienda": "www.wong.pe",
			"url": "https://www.wong.pe/papa-negra-comcen-2-kg-774132/p"
		},
		{
			"2022-11-21": "Precio Online S/ 2.68 x kg",
			"_id": "20795",
			"categoria": "frutas-y-verduras",
			"nombre": "Papa Blanca Cocktail x kg",
			"subcategoria": "verduras",
			"tienda": "www.wong.pe",
			"url": "https://www.wong.pe/papa-blanca-cocktail-x-kg-20795/p"
		},
		{
			"2022-11-21": "Precio Online S/ 3.48 x kg",
			"_id": "162060",
			"categoria": "frutas-y-verduras",
			"nombre": "Papa Blanca Yungay x kg",
			"subcategoria": "verduras",
			"tienda": "www.wong.pe",
			"url": "https://www.wong.pe/papa-blanca-yungay-x-kg-162060/p"
		},
		{
			"2022-11-21": "",
			"_id": "118",
			"categoria": "frutas-y-verduras",
			"nombre": "Papa Canchán Procesada Especial x kg",
			"subcategoria": "verduras",
			"tienda": "www.wong.pe",
			"url": "https://www.wong.pe/papa-canchan-procesada-especial-x-kg-118/p"
		},
		{
			"2022-11-21": "Precio Online S/ 8.55",
			"_id": "774130",
			"categoria": "frutas-y-verduras",
			"nombre": "Papa Canchán Procesada Comcen 2 kg",
			"subcategoria": "verduras",
			"tienda": "www.wong.pe",
			"url": "https://www.wong.pe/papa-canchan-procesada-comcen-2-kg-774130/p"
		},
		{
			"2022-11-21": "Precio Online S/ 11.70",
			"_id": "9kg",
			"categoria": "frutas-y-verduras",
			"nombre": "Papa Yungay Campo Lindo 2.9kg",
			"subcategoria": "verduras",
			"tienda": "www.wong.pe",
			"url": "https://www.wong.pe/papa-canchan-campo-lindo-malla-1-9kg/p"
		},
		{
			"2022-11-21": "Precio Online S/ 9.18",
			"_id": "902074",
			"categoria": "frutas-y-verduras",
			"nombre": "Papa Blanca Yungay Agro Selecto 2kg",
			"subcategoria": "verduras",
			"tienda": "www.wong.pe",
			"url": "https://www.wong.pe/papa-blanca-yungay-agro-selecto-2kg-902074-2/p"
		},
		{
			"2022-11-21": "Precio Online S/ 4.48 x kg",
			"_id": "162063",
			"categoria": "frutas-y-verduras",
			"nombre": "Papa Negra Andina Procesada x kg",
			"subcategoria": "verduras",
			"tienda": "www.wong.pe",
			"url": "https://www.wong.pe/papa-negra-andina-procesada-x-kg-162063/p"
		},
		{
			"2022-11-21": "Precio Online S/ 3.96 x kg",
			"_id": "4182",
			"categoria": "frutas-y-verduras",
			"nombre": "Papa Blanca Canchán Procesada x kg",
			"subcategoria": "verduras",
			"tienda": "www.wong.pe",
			"url": "https://www.wong.pe/papa-blanca-canchan-procesada-x-kg-4182/p"
		},
		{
			"2022-11-21": "Precio Online S/ 6.48",
			"_id": "800",
			"categoria": "frutas-y-verduras",
			"nombre": "Papa Tricolor Cocktail Agro Selecto 800 g",
			"subcategoria": "verduras",
			"tienda": "www.wong.pe",
			"url": "https://www.wong.pe/papa-tricolor-cocktail-agro-selecto-800-g/p"
		},
		{
			"2022-11-21": "Precio Online S/ 4.20 x kg",
			"_id": "4155",
			"categoria": "frutas-y-verduras",
			"nombre": "Papa Blanca Perricholi Procesada Wong x kg",
			"subcategoria": "verduras",
			"tienda": "www.wong.pe",
			"url": "https://www.wong.pe/papa-blanca-perricholi-procesada-wong-x-kg-4155/p"
		},
		{
			"2022-11-21": "Precio Online S/ 6.48",
			"_id": "887160",
			"categoria": "frutas-y-verduras",
			"nombre": "Papa Peruanita Cocktail Agro Selecto Ready 800g",
			"subcategoria": "verduras",
			"tienda": "www.wong.pe",
			"url": "https://www.wong.pe/papa-peruanita-cocktail-agro-selecto-ready-800g-887160-2/p"
		},
		{
			"2022-11-21": "Precio Online S/ 7.47",
			"_id": "574742",
			"categoria": "frutas-y-verduras",
			"nombre": "Papa Cocktail Blanca Campo Lindo Cocina Fácil 800g",
			"subcategoria": "verduras",
			"tienda": "www.wong.pe",
			"url": "https://www.wong.pe/papa-cocktail-blanca-campo-lindo-cocina-facil-800g-574742-2/p"
		}
	],
	"detalle": "éxito"
}


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)