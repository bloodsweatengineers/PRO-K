VERSION 	=0.01
CC 			=avr-gcc
COPY 		=avr-objcopy

BUILDDIR 	=build
OBJDIR 		=Embedded/obj
SOURCEDIR 	=Embedded/src
HEADERDIR 	=Embedded/include

PDFDIR 		=Docs/PDF
PAPERDIR 	=Docs/Paper
RAPPORTDIR  =Docs/Eindrapportage
MANUALDIR 	=Docs/Manual

GENDIR 		=Gen
GENFILE 	=generate.py
GENERATED_H =token_table.h
GENERATED_C =token.c

MKDIR 		=mkdir -p

SOURCEPATHS :=$(shell find $(SOURCEDIR) -name '*.c')
SOURCEFILES :=$(subst $(SOURCEDIR)/,,$(SOURCEPATHS))

OBJFILES 	:=$(SOURCEFILES:=.o)
OBJPATHS 	:=$(addprefix $(OBJDIR)/, $(OBJFILES))

NAME 		=executable
NAME_PATH 	=$(BUILDDIR)/$(NAME)
HEX_NAME_PATH =$(BUILDDIR)/$(NAME).hex

HEADERS 	=-I$(HEADERDIR)
CFLAGS 		=-Os -DF_CPU=16000000UL
MCUFLAGS 	=-mmcu=atmega328p

TEST_SOURCE =Test/test.c
TEST_OBJ 	=build/test 
TEST 		=build/test.hex

CUR 		=$(shell pwd)

all : directories generator $(HEX_NAME_PATH)

docs: eindrapportage

.ONESHELL:
eindrapportage:
	cd $(RAPPORTDIR)
	pdflatex main.tex
	pdflatex main.tex
	mv main.pdf $(CUR)/$(PDFDIR)/EindRapportage.pdf
	cd $(CUR)

#paper:

#manual:

generator:
	python3 $(GENDIR)/$(GENFILE) $(GENDIR) token.csv
	mv $(GENDIR)/$(GENERATED_C) $(SOURCEDIR)/
	mv $(GENDIR)/$(GENERATED_H) $(HEADERDIR)/

directories:
	$(MKDIR) $(BUILDDIR)
	$(MKDIR) $(OBJDIR)
	$(MKDIR) $(PDFDIR)

$(HEX_NAME_PATH) : $(NAME_PATH)
	$(COPY) -O ihex $< $@

$(NAME_PATH) : $(OBJPATHS)
	$(CC) -o $@ $^ $(MCUFLAGS) $(CFLAGS) $(LDFLAGS) $(HEADERS)

$(OBJDIR)/%.c.o : $(SOURCEDIR)/%.c
	$(CC) -c -o $@ $< $(MCUFLAGS) $(CFLAGS) $(LDFLAGS) $(HEADERS)

clean:
	pwd
	rm -rf $(OBJDIR)/* $(BUILDDIR)/*
	rm -rf ./*.aux ./*.log ./*.out ./*.toc

install:
	avrdude -vvv -c arduino -P /dev/ttyACM0 -p m328p -U flash:w:$(HEX_NAME_PATH)

test:
	$(CC) -o $(TEST_OBJ) $(TEST_SOURCE) $(MCUFLAGS) $(CFLAGS) $(LDFLAGS)
	$(COPY) -O ihex $(TEST_OBJ) $(TEST)
	avrdude -vvv -c arduino -P /dev/ttyACM0 -p m328p -U flash:w:$(TEST)

.PHONY: directories clean install test
