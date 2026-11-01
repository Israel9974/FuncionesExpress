from pyspark.sql import SparkSession
from pyspark.sql.functions import col

spark = SparkSession.builder.getOrCreate()

# DataFrame inicial: números del 1 al 100
df = spark.range(1, 101).toDF("n")

# Función para verificar si un número es primo
def es_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Obtener los primos en una lista
primos = [r.n for r in df.collect() if es_primo(r.n)]

# Encontrar primos gemelos
gemelos = [(p, p + 2) for p in primos if p + 2 in primos]

# Crear DataFrame resultado
df_gemelos = spark.createDataFrame(gemelos, ["primo1", "primo2"])

df_gemelos.show()


# Alternativa 

from pyspark.sql.functions import col

# DataFrame de primos
primos_df = spark.createDataFrame(
    [(n,) for n in range(2, 101) if es_primo(n)],
    ["primo"]
)

# Join consigo mismo buscando diferencia de 2
df_gemelos = (
    primos_df.alias("a")
    .join(
        primos_df.alias("b"),
        col("b.primo") == col("a.primo") + 2
    )
    .select(
        col("a.primo").alias("primo1"),
        col("b.primo").alias("primo2")
    )
)

df_gemelos.show()




