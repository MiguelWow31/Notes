
class Venezuela():

	def texto(self, nota):

		try:

			self.nota = int(nota)

			if self.nota > 0 and self.nota < 21:
				mala = "imagenes/calificacion/bueno.ico"
				intermedia = "imagenes/calificacion/intermedio.ico"
				buena = "imagenes/calificacion/malo.ico"

				if self.nota < 12:
					return buena

				elif self.nota > 11 and self.nota < 17:
					return intermedia

				elif self.nota > 16 and self.nota < 21:
					return mala

		except:
			raise ValueError

	def promedio(self, limit, list_notas):

		int_notas = map(lambda nota: int(nota), list_notas)
		promedio = sum(int_notas) / limit

		return str(promedio)


class Colombia():

	def texto(self, nota):

		self.nota = float(nota)

		if self.nota > 0.9 and self.nota < 5.1:
			mala = "imagenes/calificacion/bueno.ico"
			intermedia = "imagenes/calificacion/intermedio.ico"
			buena = "imagenes/calificacion/malo.ico"

			if self.nota > 3.9:
				return mala

			elif self.nota > 2.9 and self.nota < 4.0:
				return intermedia

			elif self.nota < 3.0:
				return buena

		else:
			raise ValueError

	def promedio(self, limit, list_notas):

		int_notas = map(lambda nota: float(nota), list_notas)
		promedio = round(sum(int_notas) / limit, 1)

		return str(promedio)

		






            