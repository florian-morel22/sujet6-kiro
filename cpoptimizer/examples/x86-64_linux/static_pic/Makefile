CXX = g++
CONCERTDIR = ../../../../concert
CPLEXDIR = ../../../../cplex
CFLAGS = -DIL_STD -O -DNDEBUG -I../../../include -I$(CONCERTDIR)/include -fPIC -fstrict-aliasing -pedantic -Wall -Wextra -fexceptions -frounding-math -Wno-long-long -m64 -DILOUSEMT -D_REENTRANT -DILM_REENTRANT -Wno-ignored-attributes
LDFLAGS = -L../../../lib/x86-64_linux/static_pic -lcp -L$(CPLEXDIR)/lib/x86-64_linux/static_pic -lcplex -L$(CONCERTDIR)/lib/x86-64_linux/static_pic -lconcert  -lpthread -lm -ldl 
JAVA = $(JAVA_HOME)/bin/java
JAVAC = $(JAVA_HOME)/bin/javac
JAVAFLAGS = -d64
CPCLASSPATH = ../../../lib/ILOG.CP.jar
LIBRARYPATH = ../../../bin/x86-64_linux:$(CPLEXDIR)/bin/x86-64_linux
CPPEXDIR = ../../../examples/src/cpp
JAVAEXDIR = ../../../examples/src/java

all: cpp java

cpp: alloc callbacks color color_ex3 color_ex4 cpofileformat facility facility_ex3 facility_ex4 facility_explanations intro networkcfg plantlocation ppp sched_calendar sched_conflict sched_cumul sched_flowshop sched_goalprog sched_intro sched_jobshop sched_jobshopflex sched_learningeffect sched_openshop sched_optional sched_pflowshop sched_rcpsp sched_rcpspmm schedsearch_greedyandrelax schedsearch_optionalsettimes schedsearch_permutation schedsearch_sequencing schedsearch_settimes sched_sequence sched_setup sched_square sched_state sched_stochastic_jobshop sched_tcost sched_time searchphases smooth sports sports_strong steelmill steelmill_ex3 talent teambuilding truckfleet

java: Alloc.class Callbacks.class Color.class CPOFileFormat.class FacilityExplanations.class Facility.class PlantLocation.class Ppp.class SchedCalendar.class SchedConflict.class SchedCumul.class SchedFlowShop.class SchedGoalProg.class SchedIntro.class SchedJobShopFlex.class SchedJobShop.class SchedLearningEffect.class SchedOpenShop.class SchedOptional.class SchedPFlowShop.class SchedRCPSP.class SchedRCPSPMM.class SchedSequence.class SchedSetup.class SchedSquare.class SchedState.class SchedStochasticJobShop.class SchedTCost.class SchedTime.class SearchPhases.class Sports.class SportsStrong.class Steelmill.class Talent.class Teambuilding.class Truckfleet.class

execute: execute_cpp execute_java

clean:
	rm -f alloc callbacks color color_ex3 color_ex4 cpofileformat facility facility_ex3 facility_ex4 facility_explanations intro networkcfg plantlocation ppp sched_calendar sched_conflict sched_cumul sched_flowshop sched_goalprog sched_intro sched_jobshop sched_jobshopflex sched_learningeffect sched_openshop sched_optional sched_pflowshop sched_rcpsp sched_rcpspmm schedsearch_greedyandrelax schedsearch_optionalsettimes schedsearch_permutation schedsearch_sequencing schedsearch_settimes sched_sequence sched_setup sched_square sched_state sched_stochastic_jobshop sched_tcost sched_time searchphases smooth sports sports_strong steelmill steelmill_ex3 talent teambuilding truckfleet *.class

.PHONY: all cpp java clean execute execute_cpp execute_java

$(JAVAC):
	@echo "####################################"
	@echo "Error: cannot find the javac command"
	@echo "Please ensure that JAVA_HOME is set correctly"
	@echo "Currently, JAVA_HOME = $(JAVA_HOME)"
	@exit 1

alloc:
	$(CXX) -o alloc $(CFLAGS) $(CPPEXDIR)/alloc.cpp $(LDFLAGS)

alloc.run: alloc
	./alloc
.PHONY: alloc.run

callbacks:
	$(CXX) -o callbacks $(CFLAGS) $(CPPEXDIR)/callbacks.cpp $(LDFLAGS)

callbacks.run: callbacks
	./callbacks
.PHONY: callbacks.run

color:
	$(CXX) -o color $(CFLAGS) $(CPPEXDIR)/color.cpp $(LDFLAGS)

color.run: color
	./color
.PHONY: color.run

color_ex3:
	$(CXX) -o color_ex3 $(CFLAGS) $(CPPEXDIR)/color_ex3.cpp $(LDFLAGS)

color_ex3.run: color_ex3
	./color_ex3
.PHONY: color_ex3.run

color_ex4:
	$(CXX) -o color_ex4 $(CFLAGS) $(CPPEXDIR)/color_ex4.cpp $(LDFLAGS)

color_ex4.run: color_ex4
	./color_ex4
.PHONY: color_ex4.run

cpofileformat:
	$(CXX) -o cpofileformat $(CFLAGS) $(CPPEXDIR)/cpofileformat.cpp $(LDFLAGS)

cpofileformat.run: cpofileformat
	./cpofileformat
.PHONY: cpofileformat.run

facility:
	$(CXX) -o facility $(CFLAGS) $(CPPEXDIR)/facility.cpp $(LDFLAGS)

facility.run: facility
	./facility
.PHONY: facility.run

facility_ex3:
	$(CXX) -o facility_ex3 $(CFLAGS) $(CPPEXDIR)/facility_ex3.cpp $(LDFLAGS)

facility_ex3.run: facility_ex3
	./facility_ex3
.PHONY: facility_ex3.run

facility_ex4:
	$(CXX) -o facility_ex4 $(CFLAGS) $(CPPEXDIR)/facility_ex4.cpp $(LDFLAGS)

facility_ex4.run: facility_ex4
	./facility_ex4
.PHONY: facility_ex4.run

facility_explanations:
	$(CXX) -o facility_explanations $(CFLAGS) $(CPPEXDIR)/facility_explanations.cpp $(LDFLAGS)

facility_explanations.run: facility_explanations
	./facility_explanations
.PHONY: facility_explanations.run

intro:
	$(CXX) -o intro $(CFLAGS) $(CPPEXDIR)/intro.cpp $(LDFLAGS)

intro.run: intro
	./intro
.PHONY: intro.run

networkcfg:
	$(CXX) -o networkcfg $(CFLAGS) $(CPPEXDIR)/networkcfg.cpp $(LDFLAGS)

networkcfg.run: networkcfg
	./networkcfg
.PHONY: networkcfg.run

plantlocation:
	$(CXX) -o plantlocation $(CFLAGS) $(CPPEXDIR)/plantlocation.cpp $(LDFLAGS)

plantlocation.run: plantlocation
	./plantlocation
.PHONY: plantlocation.run

ppp:
	$(CXX) -o ppp $(CFLAGS) $(CPPEXDIR)/ppp.cpp $(LDFLAGS)

ppp.run: ppp
	./ppp
.PHONY: ppp.run

sched_calendar:
	$(CXX) -o sched_calendar $(CFLAGS) $(CPPEXDIR)/sched_calendar.cpp $(LDFLAGS)

sched_calendar.run: sched_calendar
	./sched_calendar
.PHONY: sched_calendar.run

sched_conflict:
	$(CXX) -o sched_conflict $(CFLAGS) $(CPPEXDIR)/sched_conflict.cpp $(LDFLAGS)

sched_conflict.run: sched_conflict
	./sched_conflict
.PHONY: sched_conflict.run

sched_cumul:
	$(CXX) -o sched_cumul $(CFLAGS) $(CPPEXDIR)/sched_cumul.cpp $(LDFLAGS)

sched_cumul.run: sched_cumul
	./sched_cumul
.PHONY: sched_cumul.run

sched_flowshop:
	$(CXX) -o sched_flowshop $(CFLAGS) $(CPPEXDIR)/sched_flowshop.cpp $(LDFLAGS)

sched_flowshop.run: sched_flowshop
	./sched_flowshop
.PHONY: sched_flowshop.run

sched_goalprog:
	$(CXX) -o sched_goalprog $(CFLAGS) $(CPPEXDIR)/sched_goalprog.cpp $(LDFLAGS)

sched_goalprog.run: sched_goalprog
	./sched_goalprog
.PHONY: sched_goalprog.run

sched_intro:
	$(CXX) -o sched_intro $(CFLAGS) $(CPPEXDIR)/sched_intro.cpp $(LDFLAGS)

sched_intro.run: sched_intro
	./sched_intro
.PHONY: sched_intro.run

sched_jobshop:
	$(CXX) -o sched_jobshop $(CFLAGS) $(CPPEXDIR)/sched_jobshop.cpp $(LDFLAGS)

sched_jobshop.run: sched_jobshop
	./sched_jobshop
.PHONY: sched_jobshop.run

sched_jobshopflex:
	$(CXX) -o sched_jobshopflex $(CFLAGS) $(CPPEXDIR)/sched_jobshopflex.cpp $(LDFLAGS)

sched_jobshopflex.run: sched_jobshopflex
	./sched_jobshopflex
.PHONY: sched_jobshopflex.run

sched_learningeffect:
	$(CXX) -o sched_learningeffect $(CFLAGS) $(CPPEXDIR)/sched_learningeffect.cpp $(LDFLAGS)

sched_learningeffect.run: sched_learningeffect
	./sched_learningeffect
.PHONY: sched_learningeffect.run

sched_openshop:
	$(CXX) -o sched_openshop $(CFLAGS) $(CPPEXDIR)/sched_openshop.cpp $(LDFLAGS)

sched_openshop.run: sched_openshop
	./sched_openshop
.PHONY: sched_openshop.run

sched_optional:
	$(CXX) -o sched_optional $(CFLAGS) $(CPPEXDIR)/sched_optional.cpp $(LDFLAGS)

sched_optional.run: sched_optional
	./sched_optional
.PHONY: sched_optional.run

sched_pflowshop:
	$(CXX) -o sched_pflowshop $(CFLAGS) $(CPPEXDIR)/sched_pflowshop.cpp $(LDFLAGS)

sched_pflowshop.run: sched_pflowshop
	./sched_pflowshop
.PHONY: sched_pflowshop.run

sched_rcpsp:
	$(CXX) -o sched_rcpsp $(CFLAGS) $(CPPEXDIR)/sched_rcpsp.cpp $(LDFLAGS)

sched_rcpsp.run: sched_rcpsp
	./sched_rcpsp
.PHONY: sched_rcpsp.run

sched_rcpspmm:
	$(CXX) -o sched_rcpspmm $(CFLAGS) $(CPPEXDIR)/sched_rcpspmm.cpp $(LDFLAGS)

sched_rcpspmm.run: sched_rcpspmm
	./sched_rcpspmm
.PHONY: sched_rcpspmm.run

schedsearch_greedyandrelax:
	$(CXX) -o schedsearch_greedyandrelax $(CFLAGS) $(CPPEXDIR)/schedsearch_greedyandrelax.cpp $(LDFLAGS)

schedsearch_greedyandrelax.run: schedsearch_greedyandrelax
	./schedsearch_greedyandrelax
.PHONY: schedsearch_greedyandrelax.run

schedsearch_optionalsettimes:
	$(CXX) -o schedsearch_optionalsettimes $(CFLAGS) $(CPPEXDIR)/schedsearch_optionalsettimes.cpp $(LDFLAGS)

schedsearch_optionalsettimes.run: schedsearch_optionalsettimes
	./schedsearch_optionalsettimes
.PHONY: schedsearch_optionalsettimes.run

schedsearch_permutation:
	$(CXX) -o schedsearch_permutation $(CFLAGS) $(CPPEXDIR)/schedsearch_permutation.cpp $(LDFLAGS)

schedsearch_permutation.run: schedsearch_permutation
	./schedsearch_permutation
.PHONY: schedsearch_permutation.run

schedsearch_sequencing:
	$(CXX) -o schedsearch_sequencing $(CFLAGS) $(CPPEXDIR)/schedsearch_sequencing.cpp $(LDFLAGS)

schedsearch_sequencing.run: schedsearch_sequencing
	./schedsearch_sequencing
.PHONY: schedsearch_sequencing.run

schedsearch_settimes:
	$(CXX) -o schedsearch_settimes $(CFLAGS) $(CPPEXDIR)/schedsearch_settimes.cpp $(LDFLAGS)

schedsearch_settimes.run: schedsearch_settimes
	./schedsearch_settimes
.PHONY: schedsearch_settimes.run

sched_sequence:
	$(CXX) -o sched_sequence $(CFLAGS) $(CPPEXDIR)/sched_sequence.cpp $(LDFLAGS)

sched_sequence.run: sched_sequence
	./sched_sequence
.PHONY: sched_sequence.run

sched_setup:
	$(CXX) -o sched_setup $(CFLAGS) $(CPPEXDIR)/sched_setup.cpp $(LDFLAGS)

sched_setup.run: sched_setup
	./sched_setup
.PHONY: sched_setup.run

sched_square:
	$(CXX) -o sched_square $(CFLAGS) $(CPPEXDIR)/sched_square.cpp $(LDFLAGS)

sched_square.run: sched_square
	./sched_square
.PHONY: sched_square.run

sched_state:
	$(CXX) -o sched_state $(CFLAGS) $(CPPEXDIR)/sched_state.cpp $(LDFLAGS)

sched_state.run: sched_state
	./sched_state
.PHONY: sched_state.run

sched_stochastic_jobshop:
	$(CXX) -o sched_stochastic_jobshop $(CFLAGS) $(CPPEXDIR)/sched_stochastic_jobshop.cpp $(LDFLAGS)

sched_stochastic_jobshop.run: sched_stochastic_jobshop
	./sched_stochastic_jobshop
.PHONY: sched_stochastic_jobshop.run

sched_tcost:
	$(CXX) -o sched_tcost $(CFLAGS) $(CPPEXDIR)/sched_tcost.cpp $(LDFLAGS)

sched_tcost.run: sched_tcost
	./sched_tcost
.PHONY: sched_tcost.run

sched_time:
	$(CXX) -o sched_time $(CFLAGS) $(CPPEXDIR)/sched_time.cpp $(LDFLAGS)

sched_time.run: sched_time
	./sched_time
.PHONY: sched_time.run

searchphases:
	$(CXX) -o searchphases $(CFLAGS) $(CPPEXDIR)/searchphases.cpp $(LDFLAGS)

searchphases.run: searchphases
	./searchphases
.PHONY: searchphases.run

smooth:
	$(CXX) -o smooth $(CFLAGS) $(CPPEXDIR)/smooth.cpp $(LDFLAGS)

smooth.run: smooth
	./smooth
.PHONY: smooth.run

sports:
	$(CXX) -o sports $(CFLAGS) $(CPPEXDIR)/sports.cpp $(LDFLAGS)

sports.run: sports
	./sports
.PHONY: sports.run

sports_strong:
	$(CXX) -o sports_strong $(CFLAGS) $(CPPEXDIR)/sports_strong.cpp $(LDFLAGS)

sports_strong.run: sports_strong
	./sports_strong
.PHONY: sports_strong.run

steelmill:
	$(CXX) -o steelmill $(CFLAGS) $(CPPEXDIR)/steelmill.cpp $(LDFLAGS)

steelmill.run: steelmill
	./steelmill
.PHONY: steelmill.run

steelmill_ex3:
	$(CXX) -o steelmill_ex3 $(CFLAGS) $(CPPEXDIR)/steelmill_ex3.cpp $(LDFLAGS)

steelmill_ex3.run: steelmill_ex3
	./steelmill_ex3
.PHONY: steelmill_ex3.run

talent:
	$(CXX) -o talent $(CFLAGS) $(CPPEXDIR)/talent.cpp $(LDFLAGS)

talent.run: talent
	./talent
.PHONY: talent.run

teambuilding:
	$(CXX) -o teambuilding $(CFLAGS) $(CPPEXDIR)/teambuilding.cpp $(LDFLAGS)

teambuilding.run: teambuilding
	./teambuilding
.PHONY: teambuilding.run

truckfleet:
	$(CXX) -o truckfleet $(CFLAGS) $(CPPEXDIR)/truckfleet.cpp $(LDFLAGS)

truckfleet.run: truckfleet
	./truckfleet
.PHONY: truckfleet.run

execute_cpp: alloc.run callbacks.run color.run color_ex3.run color_ex4.run cpofileformat.run facility.run facility_ex3.run facility_ex4.run facility_explanations.run intro.run networkcfg.run plantlocation.run ppp.run sched_calendar.run sched_conflict.run sched_cumul.run sched_flowshop.run sched_goalprog.run sched_intro.run sched_jobshop.run sched_jobshopflex.run sched_learningeffect.run sched_openshop.run sched_optional.run sched_pflowshop.run sched_rcpsp.run sched_rcpspmm.run schedsearch_greedyandrelax.run schedsearch_optionalsettimes.run schedsearch_permutation.run schedsearch_sequencing.run schedsearch_settimes.run sched_sequence.run sched_setup.run sched_square.run sched_state.run sched_stochastic_jobshop.run sched_tcost.run sched_time.run searchphases.run smooth.run sports.run sports_strong.run steelmill.run steelmill_ex3.run talent.run teambuilding.run truckfleet.run

Alloc.class: $(JAVAC)
	$(JAVAC) -d . -classpath $(CPCLASSPATH) $(JAVAEXDIR)/Alloc.java

Alloc.run: Alloc.class
	LD_LIBRARY_PATH=$(LIBRARYPATH) $(JAVA) $(JAVAFLAGS) -classpath $(CPCLASSPATH):. Alloc
.PHONY: Alloc.run

Callbacks.class: $(JAVAC)
	$(JAVAC) -d . -classpath $(CPCLASSPATH) $(JAVAEXDIR)/Callbacks.java

Callbacks.run: Callbacks.class
	LD_LIBRARY_PATH=$(LIBRARYPATH) $(JAVA) $(JAVAFLAGS) -classpath $(CPCLASSPATH):. Callbacks
.PHONY: Callbacks.run

Color.class: $(JAVAC)
	$(JAVAC) -d . -classpath $(CPCLASSPATH) $(JAVAEXDIR)/Color.java

Color.run: Color.class
	LD_LIBRARY_PATH=$(LIBRARYPATH) $(JAVA) $(JAVAFLAGS) -classpath $(CPCLASSPATH):. Color
.PHONY: Color.run

CPOFileFormat.class: $(JAVAC)
	$(JAVAC) -d . -classpath $(CPCLASSPATH) $(JAVAEXDIR)/CPOFileFormat.java

CPOFileFormat.run: CPOFileFormat.class
	LD_LIBRARY_PATH=$(LIBRARYPATH) $(JAVA) $(JAVAFLAGS) -classpath $(CPCLASSPATH):. CPOFileFormat
.PHONY: CPOFileFormat.run

FacilityExplanations.class: $(JAVAC)
	$(JAVAC) -d . -classpath $(CPCLASSPATH) $(JAVAEXDIR)/FacilityExplanations.java

FacilityExplanations.run: FacilityExplanations.class
	LD_LIBRARY_PATH=$(LIBRARYPATH) $(JAVA) $(JAVAFLAGS) -classpath $(CPCLASSPATH):. FacilityExplanations
.PHONY: FacilityExplanations.run

Facility.class: $(JAVAC)
	$(JAVAC) -d . -classpath $(CPCLASSPATH) $(JAVAEXDIR)/Facility.java

Facility.run: Facility.class
	LD_LIBRARY_PATH=$(LIBRARYPATH) $(JAVA) $(JAVAFLAGS) -classpath $(CPCLASSPATH):. Facility
.PHONY: Facility.run

PlantLocation.class: $(JAVAC)
	$(JAVAC) -d . -classpath $(CPCLASSPATH) $(JAVAEXDIR)/PlantLocation.java

PlantLocation.run: PlantLocation.class
	LD_LIBRARY_PATH=$(LIBRARYPATH) $(JAVA) $(JAVAFLAGS) -classpath $(CPCLASSPATH):. PlantLocation
.PHONY: PlantLocation.run

Ppp.class: $(JAVAC)
	$(JAVAC) -d . -classpath $(CPCLASSPATH) $(JAVAEXDIR)/Ppp.java

Ppp.run: Ppp.class
	LD_LIBRARY_PATH=$(LIBRARYPATH) $(JAVA) $(JAVAFLAGS) -classpath $(CPCLASSPATH):. Ppp
.PHONY: Ppp.run

SchedCalendar.class: $(JAVAC)
	$(JAVAC) -d . -classpath $(CPCLASSPATH) $(JAVAEXDIR)/SchedCalendar.java

SchedCalendar.run: SchedCalendar.class
	LD_LIBRARY_PATH=$(LIBRARYPATH) $(JAVA) $(JAVAFLAGS) -classpath $(CPCLASSPATH):. SchedCalendar
.PHONY: SchedCalendar.run

SchedConflict.class: $(JAVAC)
	$(JAVAC) -d . -classpath $(CPCLASSPATH) $(JAVAEXDIR)/SchedConflict.java

SchedConflict.run: SchedConflict.class
	LD_LIBRARY_PATH=$(LIBRARYPATH) $(JAVA) $(JAVAFLAGS) -classpath $(CPCLASSPATH):. SchedConflict
.PHONY: SchedConflict.run

SchedCumul.class: $(JAVAC)
	$(JAVAC) -d . -classpath $(CPCLASSPATH) $(JAVAEXDIR)/SchedCumul.java

SchedCumul.run: SchedCumul.class
	LD_LIBRARY_PATH=$(LIBRARYPATH) $(JAVA) $(JAVAFLAGS) -classpath $(CPCLASSPATH):. SchedCumul
.PHONY: SchedCumul.run

SchedFlowShop.class: $(JAVAC)
	$(JAVAC) -d . -classpath $(CPCLASSPATH) $(JAVAEXDIR)/SchedFlowShop.java

SchedFlowShop.run: SchedFlowShop.class
	LD_LIBRARY_PATH=$(LIBRARYPATH) $(JAVA) $(JAVAFLAGS) -classpath $(CPCLASSPATH):. SchedFlowShop
.PHONY: SchedFlowShop.run

SchedGoalProg.class: $(JAVAC)
	$(JAVAC) -d . -classpath $(CPCLASSPATH) $(JAVAEXDIR)/SchedGoalProg.java

SchedGoalProg.run: SchedGoalProg.class
	LD_LIBRARY_PATH=$(LIBRARYPATH) $(JAVA) $(JAVAFLAGS) -classpath $(CPCLASSPATH):. SchedGoalProg
.PHONY: SchedGoalProg.run

SchedIntro.class: $(JAVAC)
	$(JAVAC) -d . -classpath $(CPCLASSPATH) $(JAVAEXDIR)/SchedIntro.java

SchedIntro.run: SchedIntro.class
	LD_LIBRARY_PATH=$(LIBRARYPATH) $(JAVA) $(JAVAFLAGS) -classpath $(CPCLASSPATH):. SchedIntro
.PHONY: SchedIntro.run

SchedJobShopFlex.class: $(JAVAC)
	$(JAVAC) -d . -classpath $(CPCLASSPATH) $(JAVAEXDIR)/SchedJobShopFlex.java

SchedJobShopFlex.run: SchedJobShopFlex.class
	LD_LIBRARY_PATH=$(LIBRARYPATH) $(JAVA) $(JAVAFLAGS) -classpath $(CPCLASSPATH):. SchedJobShopFlex
.PHONY: SchedJobShopFlex.run

SchedJobShop.class: $(JAVAC)
	$(JAVAC) -d . -classpath $(CPCLASSPATH) $(JAVAEXDIR)/SchedJobShop.java

SchedJobShop.run: SchedJobShop.class
	LD_LIBRARY_PATH=$(LIBRARYPATH) $(JAVA) $(JAVAFLAGS) -classpath $(CPCLASSPATH):. SchedJobShop
.PHONY: SchedJobShop.run

SchedLearningEffect.class: $(JAVAC)
	$(JAVAC) -d . -classpath $(CPCLASSPATH) $(JAVAEXDIR)/SchedLearningEffect.java

SchedLearningEffect.run: SchedLearningEffect.class
	LD_LIBRARY_PATH=$(LIBRARYPATH) $(JAVA) $(JAVAFLAGS) -classpath $(CPCLASSPATH):. SchedLearningEffect
.PHONY: SchedLearningEffect.run

SchedOpenShop.class: $(JAVAC)
	$(JAVAC) -d . -classpath $(CPCLASSPATH) $(JAVAEXDIR)/SchedOpenShop.java

SchedOpenShop.run: SchedOpenShop.class
	LD_LIBRARY_PATH=$(LIBRARYPATH) $(JAVA) $(JAVAFLAGS) -classpath $(CPCLASSPATH):. SchedOpenShop
.PHONY: SchedOpenShop.run

SchedOptional.class: $(JAVAC)
	$(JAVAC) -d . -classpath $(CPCLASSPATH) $(JAVAEXDIR)/SchedOptional.java

SchedOptional.run: SchedOptional.class
	LD_LIBRARY_PATH=$(LIBRARYPATH) $(JAVA) $(JAVAFLAGS) -classpath $(CPCLASSPATH):. SchedOptional
.PHONY: SchedOptional.run

SchedPFlowShop.class: $(JAVAC)
	$(JAVAC) -d . -classpath $(CPCLASSPATH) $(JAVAEXDIR)/SchedPFlowShop.java

SchedPFlowShop.run: SchedPFlowShop.class
	LD_LIBRARY_PATH=$(LIBRARYPATH) $(JAVA) $(JAVAFLAGS) -classpath $(CPCLASSPATH):. SchedPFlowShop
.PHONY: SchedPFlowShop.run

SchedRCPSP.class: $(JAVAC)
	$(JAVAC) -d . -classpath $(CPCLASSPATH) $(JAVAEXDIR)/SchedRCPSP.java

SchedRCPSP.run: SchedRCPSP.class
	LD_LIBRARY_PATH=$(LIBRARYPATH) $(JAVA) $(JAVAFLAGS) -classpath $(CPCLASSPATH):. SchedRCPSP
.PHONY: SchedRCPSP.run

SchedRCPSPMM.class: $(JAVAC)
	$(JAVAC) -d . -classpath $(CPCLASSPATH) $(JAVAEXDIR)/SchedRCPSPMM.java

SchedRCPSPMM.run: SchedRCPSPMM.class
	LD_LIBRARY_PATH=$(LIBRARYPATH) $(JAVA) $(JAVAFLAGS) -classpath $(CPCLASSPATH):. SchedRCPSPMM
.PHONY: SchedRCPSPMM.run

SchedSequence.class: $(JAVAC)
	$(JAVAC) -d . -classpath $(CPCLASSPATH) $(JAVAEXDIR)/SchedSequence.java

SchedSequence.run: SchedSequence.class
	LD_LIBRARY_PATH=$(LIBRARYPATH) $(JAVA) $(JAVAFLAGS) -classpath $(CPCLASSPATH):. SchedSequence
.PHONY: SchedSequence.run

SchedSetup.class: $(JAVAC)
	$(JAVAC) -d . -classpath $(CPCLASSPATH) $(JAVAEXDIR)/SchedSetup.java

SchedSetup.run: SchedSetup.class
	LD_LIBRARY_PATH=$(LIBRARYPATH) $(JAVA) $(JAVAFLAGS) -classpath $(CPCLASSPATH):. SchedSetup
.PHONY: SchedSetup.run

SchedSquare.class: $(JAVAC)
	$(JAVAC) -d . -classpath $(CPCLASSPATH) $(JAVAEXDIR)/SchedSquare.java

SchedSquare.run: SchedSquare.class
	LD_LIBRARY_PATH=$(LIBRARYPATH) $(JAVA) $(JAVAFLAGS) -classpath $(CPCLASSPATH):. SchedSquare
.PHONY: SchedSquare.run

SchedState.class: $(JAVAC)
	$(JAVAC) -d . -classpath $(CPCLASSPATH) $(JAVAEXDIR)/SchedState.java

SchedState.run: SchedState.class
	LD_LIBRARY_PATH=$(LIBRARYPATH) $(JAVA) $(JAVAFLAGS) -classpath $(CPCLASSPATH):. SchedState
.PHONY: SchedState.run

SchedStochasticJobShop.class: $(JAVAC)
	$(JAVAC) -d . -classpath $(CPCLASSPATH) $(JAVAEXDIR)/SchedStochasticJobShop.java

SchedStochasticJobShop.run: SchedStochasticJobShop.class
	LD_LIBRARY_PATH=$(LIBRARYPATH) $(JAVA) $(JAVAFLAGS) -classpath $(CPCLASSPATH):. SchedStochasticJobShop
.PHONY: SchedStochasticJobShop.run

SchedTCost.class: $(JAVAC)
	$(JAVAC) -d . -classpath $(CPCLASSPATH) $(JAVAEXDIR)/SchedTCost.java

SchedTCost.run: SchedTCost.class
	LD_LIBRARY_PATH=$(LIBRARYPATH) $(JAVA) $(JAVAFLAGS) -classpath $(CPCLASSPATH):. SchedTCost
.PHONY: SchedTCost.run

SchedTime.class: $(JAVAC)
	$(JAVAC) -d . -classpath $(CPCLASSPATH) $(JAVAEXDIR)/SchedTime.java

SchedTime.run: SchedTime.class
	LD_LIBRARY_PATH=$(LIBRARYPATH) $(JAVA) $(JAVAFLAGS) -classpath $(CPCLASSPATH):. SchedTime
.PHONY: SchedTime.run

SearchPhases.class: $(JAVAC)
	$(JAVAC) -d . -classpath $(CPCLASSPATH) $(JAVAEXDIR)/SearchPhases.java

SearchPhases.run: SearchPhases.class
	LD_LIBRARY_PATH=$(LIBRARYPATH) $(JAVA) $(JAVAFLAGS) -classpath $(CPCLASSPATH):. SearchPhases
.PHONY: SearchPhases.run

Sports.class: $(JAVAC)
	$(JAVAC) -d . -classpath $(CPCLASSPATH) $(JAVAEXDIR)/Sports.java

Sports.run: Sports.class
	LD_LIBRARY_PATH=$(LIBRARYPATH) $(JAVA) $(JAVAFLAGS) -classpath $(CPCLASSPATH):. Sports
.PHONY: Sports.run

SportsStrong.class: $(JAVAC)
	$(JAVAC) -d . -classpath $(CPCLASSPATH) $(JAVAEXDIR)/SportsStrong.java

SportsStrong.run: SportsStrong.class
	LD_LIBRARY_PATH=$(LIBRARYPATH) $(JAVA) $(JAVAFLAGS) -classpath $(CPCLASSPATH):. SportsStrong
.PHONY: SportsStrong.run

Steelmill.class: $(JAVAC)
	$(JAVAC) -d . -classpath $(CPCLASSPATH) $(JAVAEXDIR)/Steelmill.java

Steelmill.run: Steelmill.class
	LD_LIBRARY_PATH=$(LIBRARYPATH) $(JAVA) $(JAVAFLAGS) -classpath $(CPCLASSPATH):. Steelmill
.PHONY: Steelmill.run

Talent.class: $(JAVAC)
	$(JAVAC) -d . -classpath $(CPCLASSPATH) $(JAVAEXDIR)/Talent.java

Talent.run: Talent.class
	LD_LIBRARY_PATH=$(LIBRARYPATH) $(JAVA) $(JAVAFLAGS) -classpath $(CPCLASSPATH):. Talent
.PHONY: Talent.run

Teambuilding.class: $(JAVAC)
	$(JAVAC) -d . -classpath $(CPCLASSPATH) $(JAVAEXDIR)/Teambuilding.java

Teambuilding.run: Teambuilding.class
	LD_LIBRARY_PATH=$(LIBRARYPATH) $(JAVA) $(JAVAFLAGS) -classpath $(CPCLASSPATH):. Teambuilding
.PHONY: Teambuilding.run

Truckfleet.class: $(JAVAC)
	$(JAVAC) -d . -classpath $(CPCLASSPATH) $(JAVAEXDIR)/Truckfleet.java

Truckfleet.run: Truckfleet.class
	LD_LIBRARY_PATH=$(LIBRARYPATH) $(JAVA) $(JAVAFLAGS) -classpath $(CPCLASSPATH):. Truckfleet
.PHONY: Truckfleet.run

execute_java: Alloc.run Callbacks.run Color.run CPOFileFormat.run FacilityExplanations.run Facility.run PlantLocation.run Ppp.run SchedCalendar.run SchedConflict.run SchedCumul.run SchedFlowShop.run SchedGoalProg.run SchedIntro.run SchedJobShopFlex.run SchedJobShop.run SchedLearningEffect.run SchedOpenShop.run SchedOptional.run SchedPFlowShop.run SchedRCPSP.run SchedRCPSPMM.run SchedSequence.run SchedSetup.run SchedSquare.run SchedState.run SchedStochasticJobShop.run SchedTCost.run SchedTime.run SearchPhases.run Sports.run SportsStrong.run Steelmill.run Talent.run Teambuilding.run Truckfleet.run

