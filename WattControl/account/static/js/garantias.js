
document.addEventListener('DOMContentLoaded', function() {
  // Agregar evento para filtrar productos al escribir en el campo de búsqueda
 


  // Event listener para mostrar detalles de producto al pasar el ratón
  const productos = document.querySelectorAll('.itemGarantias');

  productos.forEach(producto => {
      const infoAdicional = producto.querySelector('.detallesGarantias');

      producto.addEventListener('mouseenter', function() {
          infoAdicional.style.display = 'block';
      });

      producto.addEventListener('mouseleave', function() {
          infoAdicional.style.display = 'none';
      });
  });





  const ctxPie = document.getElementById('energyChart').getContext('2d');
    const ctxBar = document.getElementById('powerChart').getContext('2d');
    
    // Datos ficticios del consumo energético
    const dataCurrentMonth = 350; // kWh
    const dataPreviousMonth = 300; // kWh
    const costPerKWh = 2.5; // Costo por kWh en MXN
    const co2PerKWh = 0.5; // Emisiones de CO2 por kWh en kg

    // Calcular costo y emisiones
    const currentCost = (dataCurrentMonth * costPerKWh).toFixed(2);
    const currentEmissions = (dataCurrentMonth * co2PerKWh).toFixed(2);

    // Actualizar DOM con costo y emisiones
    document.getElementById('cost').textContent = Costo: $${currentCost} MXN;
    document.getElementById('emissions').textContent = Emisiones de CO2: ${currentEmissions} kg;

    // Configuración del gráfico circular
    const dataPie = {
        labels: ['Mes Actual', 'Mes Anterior'],
        datasets: [{
            data: [dataCurrentMonth, dataPreviousMonth],
            backgroundColor: ['#FFD700', '#000080'], // Amarillo y azul marino
        }]
    };

    const optionsPie = {
        responsive: true,
        plugins: {
            legend: {
                position: 'top',
            },
            tooltip: {
                callbacks: {
                    label: function (context) {
                        const label = context.label || '';
                        const value = context.raw || 0;
                        return ${label}: ${value} kWh;
                    }
                }
            },
            datalabels: {
                color: '#ffffff',
                font: {
                    weight: 'bold',
                    size: 16,
                },
                formatter: (value, context) => {
                    return ${value} kWh;
                },
                anchor: 'end',
                align: 'start',
                offset: 10
            }
        }
    };

    // Crear el gráfico circular
    new Chart(ctxPie, {
        type: 'pie',
        data: dataPie,
        options: optionsPie,
        plugins: [ChartDataLabels]
    });

    // Datos ficticios de potencia diaria
    const days = Array.from({ length: 30 }, (_, i) => i + 1);
    const powerData = days.map(() => Math.floor(Math.random() * 4000)); // Datos aleatorios de 0 a 4000 kW

    // Configuración del gráfico de barras
    const dataBar = {
        labels: days,
        datasets: [{
            label: 'Potencia (kW)',
            data: powerData,
            backgroundColor: '#FFD700' // Amarillo
        }]
    };

    const optionsBar = {
        responsive: true,
        scales: {
            x: {
                title: {
                    display: true,
                    text: 'Mayo' // Añadir el mes de mayo como título del eje x
                },
                ticks: {
                    callback: function(value, index, values) {
                        return [1, 8, 15, 22, 30].includes(value) ? value : '';
                    }
                }
            },
            y: {
                beginAtZero: true,
                max: 4000,
                title: {
                    display: true,
                    text: 'Potencia (kW)'
                }
            }
        },
        plugins: {
            legend: {
                display: false
            }
        }
    };

    // Crear el gráfico de barras
    new Chart(ctxBar, {
        type: 'bar',
        data: dataBar,
        options: optionsBar
    });
});