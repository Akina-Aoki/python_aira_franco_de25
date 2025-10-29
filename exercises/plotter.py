class AnnotatePlot:
    pass

np.random.seed(42)
x = np.linspace(0, 10, 100)
y = 2 * x + 5 + np.random.normal(0, 2, size=len(x))

annotate = AnnotatePlot(fig, ax)
annotate.arrow("Big dip here", (8, 10), (7.5, 14.8))