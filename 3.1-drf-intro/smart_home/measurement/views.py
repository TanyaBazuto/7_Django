from rest_framework.response import Response
from measurement.models import Sensor, Measurement
from measurement.serializers import SensorDetailSerializer, MeasurementSerializer, SensorSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView, RetrieveUpdateAPIView


# Получить список датчиков, создать датчик
class SensorView(ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer
    def post(self, request, *args, **kwargs):
        sensor_form = Sensor.objects.create(
            name=request.data['name'],
            description=request.data['description']
        )
        return self.create(request, sensor_form)


# Изменить датчик
class SensorUpdateView(RetrieveUpdateAPIView):
    def get_sensor(self, pk):
        return Sensor.objects.get(pk=pk)
    def patch(self, request, pk):
        update_sensor = self.get_sensor(pk)
        serializer = SensorDetailSerializer(update_sensor, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)


# Добавить измерение
class MeasurementView(ListCreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer
    def post(self, request):
        measure = MeasurementSerializer(data=request.data)
        if measure.is_valid():
            measure.save()
        return Response(data=measure.data)


# Получить информацию по датчику
class SensorInfoView(ListCreateAPIView):
    def get(self, request, pk):
        info_sensor = SensorDetailSerializer(Sensor.objects.get(pk=pk))
        return Response(data=info_sensor.data)
