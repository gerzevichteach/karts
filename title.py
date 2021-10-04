def title(index):
    str_text = "$problem_text = '"
    if index == '1':
        str_text += '<strong>ПОЛОЖЕНИЕ ТОЧЕК В ПРОСТРАНСТВЕ</strong><br />' \
               'На карточках изображено положение трех точек — А, В и N в ' \
               'пространстве относительно координатных осей OXYZ и показана ' \
               'проекция каждой точки на плоскости XOY.<br />' 
              
    elif index == '2':
        str_text += ''
    elif index == '3':
        str_text += ''
    elif index == '4':
        str_text += '<strong>ГРАФИК ДВИЖЕНИЯ</strong><br />' \
               'На карточке изображен график зависимости пути от времени ' \
               'для прямолинейного равномерного движения до остановки в одном направлении, ' \
               'после — в обратном. Необходимые расчеты к вопросам 7 - 11, 14, 15 выполнить в тетради.' 
              
    elif index == '5':
        str_text += '<strong>ГРАФИК СКОРОСТИ</strong><br />' \
               'На карточке изображен графики скорости тела.' \
               ' Указаны масса тела и сила сопротивления (трение и сопротивление среды).' 
              
    elif index == '6':
        str_text += '<strong>ВРАЩЕНИЕ ДЕТАЛЕЙ МАШИН</strong><br />' \
               'На карточке изображена конкретная машина или ' \
               'отдельный механизм с вращающимися деталями и тахометры. ' \
               'По шкале тахометра нужно определить число оборотов в минуту вращающейся детали, ' \
               'найдя предварительно цену деления шкалы прибора.' 
               
    elif index == '7':
        str_text += '<strong>ГРАФИКИ СКОРОСТЕЙ ВЗАИМОДЕЙСТВУЮЩИХ ТЕЛ</strong><br />' \
               'На карточке показаны графики скоростей взаимодействующих тел. ' \
               'В карточках № 1,4, 6, 7, 10 изображены случаи разделения одного тела на два неравной массы, ' \
               'которые движутся в противоположных направлениях после разделения. ' \
               'В остальных номерах карточек даны взаимодействия двух тел, движущихся с различными скоростями. ' \
               'Для всех карточек имеется в виду, что во время взаимодействия сила и ускорение остаются неизменными. ' 
               
    elif index == '8':
        str_text += '<strong>ДИНАМОМЕТРЫ</strong><br />' \
               'На карточке схематически изображен динамометр, к крючку которого подвешено тело. ' \
               'Рядом изображено тело с указанием линейных размеров в миллиметрах. ' 
               
    elif index == '9':
        str_text += ''
    elif index == '10':
        str_text += ''
        
    return str_text + "<br />'<strong><em>Желаем успеха!</em></strong><br />';"