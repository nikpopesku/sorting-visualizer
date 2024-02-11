from django.shortcuts import render
from os.path import abspath


def homepage(request):
    """Render homepage."""
    from pygnuplot import gnuplot

    # py-gnuplot: A quick demo

    # Ceate a gnuplot context. with "log = True" to print the gnuplot execute log.
    g = gnuplot.Gnuplot(log=True)

    # Set plotting style
    g.set(terminal='pngcairo transparent enhanced font "arial,8" fontscale 1.0 size 512, 280 ',
          output='"visualizer/static/visualizer/img/quick_example.png"',
          style=["fill transparent solid 0.50 noborder", "data lines", "function filledcurves y1=0"],
          key='title "Gaussian Distribution" center fixed left top vertical Left reverse enhanced autotitle nobox noinvert samplen 1 spacing 1 width 0 height 0',
          title='"Transparent filled curves"',
          xrange='[ -5.00000 : 5.00000 ] noreverse nowriteback',
          yrange='[ 0.00000 : 1.00000 ] noreverse nowriteback')

    # Expressions and caculations
    g.cmd('Gauss(x,mu,sigma) = 1./(sigma*sqrt(2*pi)) * exp( -(x-mu)**2 / (2*sigma**2) )',
          'd1(x) = Gauss(x, 0.5, 0.5)',
          'd2(x) = Gauss(x,  2.,  1.)',
          'd3(x) = Gauss(x, -1.,  2.)')

    # Plotting
    g.plot('d1(x) fs solid 1.0 lc rgb "forest-green" title "μ =  0.5 σ = 0.5"',
           'd2(x) lc rgb "gold" title "μ =  2.0 σ = 1.0"',
           'd3(x) lc rgb "dark-violet" title "μ = -1.0 σ = 2.0"')

    return render(request, "homepage.html")
