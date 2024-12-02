flowchart TB
 subgraph s1["Кипятим воду"]
        classDef yes fill:#71B378,color:#fff

        water["Наливаем воду"]

        start["Чайник работает?"]
        start@{shape: diam}

        water --> start
        start --> |да| yes1
        start --> |нет| no1
        yes1["Включаем чайник"]:::yes -->
        yes2["Ждём N минут"]:::yes
        

        no1["Включён ли в сеть?"]
        no1@{shape: diam}
        no1 --> |Да| no2
        no1 --> |нет| no11
        no11["Включить в сеть"] --> start
        no2["Оставить и потом отнести в ремонт"] -->
        no3["Вскипятить воду на плите"]:::yes

        yes2 ==> finish
        no3 ==> finish

        finish["Завариваем чай!"]:::yes

  end
