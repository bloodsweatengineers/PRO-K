VERSION 	=0.01
CC 			=avr-gcc
COPY 		=avr-objcopy

BUILDDIR 	=../build
OBJDIR 		=./obj
SOURCEDIR 	=./src
HEADERDIR 	=./include

SOURCEPATHS :=$(shell find $(SOURCEDIR) -name '*.c')
SOURCEFILES :=$(subst $(SOURCEDIR)/,,$(SOURCEPATHS))

OBJFILES 	:=$(SOURCEFILES:=.o)
OBJPATHS 	:=$(addprefix $(OBJDIR)/, $(OBJFILES))

NAME 		=executable
NAME_PATH 	=$(BUILDDIR)/$(NAME)
HEX_NAME_PATH =$(BUILDDIR)/$(NAME).hex

HEADERS 	=-I$(HEADERDIR)
CFLAGS 		=-DF_CPU=16000000UL
MCUFLAGS 	=-mmcu=atmega328p

all : $(HEX_NAME_PATH)

$(HEX_NAME_PATH) : $(NAME_PATH)
	$(COPY) -O ihex $< $@

$(NAME_PATH) : $(OBJPATHS)
	$(CC) -o $@ $< $(MCUFLAGS) $(CFLAGS) $(LDFLAGS) $(HEADERS)

$(OBJDIR)/%.c.o : $(SOURCEDIR)/%.c
	$(CC) -c -o $@ $< $(MCUFLAGS) $(CFLAGS) $(LDFLAGS) $(HEADERS)

clean:
	rm -rf $(OBJDIR)/* $(BUILDDIR)/*
