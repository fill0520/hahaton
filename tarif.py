
[{ 
	"Info": {
      "Name":"Ozgocho", #название
      "Requires":"0", #при единице не взимает абонплату за дни без использования пакетов
      "PaymentDay":"-1", #абонплата
      "Reset":"-1" #сброс пакетов. -1 не сбрасывает, n сбрасывает каждые n дней
	},

	"Call": {
	  "Free":"-1", #бесплатные секунды вне зависимости от времени суток
	  "Free1":"-1", #17:00-00:00, бесплатные секунды
	  "Free2":"-1", #00:00-17:00, бесплатные секунды
	  "FreeOut":"-1", #бесплатные секунды на не О!
	  "Cost":"0.02", #стоимость секунды в сети
	  "CostOut":"0.1" #стоимость секунды вне сети
	},

	"Internet": {
      "Free":"-1", #бесплатные мегабайты интернета
	  "Cost":"0.1" #стоимость за каждые 0.1 мегабайт
	},

	"SMS": {
	  "Free":"-1", #бесплатные смс вне зависимости от времени
	  "Free1":"-1", #17:00 - 00:00 бесплатные смс
	  "Free2":"-1", #00:00 - 17:00 смс
	  "FreeOut":"-1", #бесплатные смс вне сети
	  "Cost":"1.5" #стоимость ВСЕХ смс
	}

},
{ 
	"Info": {
      "Name":"Onoi",
      "Requires":"1",
      "PaymentDay":"2.99",
      "Reset":"1"
	},

	"Call": {
	  "Free":"300",
	  "Free1":"-1",
	  "Free2":"-1",
	  "FreeOut":"-1",
	  "Cost":"0.0197",
	  "CostOut":"0.0832"
	},

	"Internet": {
      "Free":"-1",
	  "Cost":"0.299"
	},

	"SMS": {
	  "Free":"5",
	  "Free1":"-1",
	  "Free2":"-1",
	  "FreeOut":"-1",
	  "Cost":"1.5"
	}

},
{ 
	"Info": {
      "Name":"Paidaluu",
      "Requires":"0",
      "PaymentDay":"3.33",
      "Reset":"-1"
	},

	"Call": {
	  "Free":"6000",
	  "Free1":"-1",
	  "Free2":"-1",
	  "FreeOut":"-1",
	  "Cost":"0.0225",
	  "CostOut":"0.09"
	},

	"Internet": {
      "Free":"-1",
	  "Cost":"0.1"
	},

	"SMS": {
	  "Free":"-1",
	  "Free1":"-1",
	  "Free2":"-1",
	  "FreeOut":"-1",
	  "Cost":"1.5"
	}

},
{ 
	"Info": {
      "Name":"PerehodiNaO!95",
      "Requires":"0",
      "PaymentDay":"13.6",
      "Reset":"7"
	},

	"Call": {
	  "Free":"-1",
	  "Free1":"1200",
	  "Free2":"10800",
	  "FreeOut":"300",
	  "Cost":"0.0197",
	  "CostOut":"0.082"
	},

	"Internet": {
      "Free":"-1",
	  "Cost":"0"
	},

	"SMS": {
	  "Free":"-1",
	  "Free1":"40",
	  "Free2":"140",
	  "FreeOut":"5",
	  "Cost":"1.5"
	}

},
{ 
	"Info": {
      "Name":"PerehodiNaO!135",
      "Requires":"0",
      "PaymentDay":"19.3",
      "Reset":"7"
	},

	"Call": {
	  "Free":"-1",
	  "Free1":"1200",
	  "Free2":"10800",
	  "FreeOut":"300",
	  "Cost":"0.0197",
	  "CostOut":"0.082"
	},

	"Internet": {
      "Free":"-1",
	  "Cost":"0"
	},

	"SMS": {
	  "Free":"-1",
	  "Free1":"40",
	  "Free2":"140",
	  "FreeOut":"5",
	  "Cost":"1.5"
	}

},
 ]
