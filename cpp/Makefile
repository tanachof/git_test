CC = g++ 
CFLAGS = 
TARGET = test
SRCS = main.cpp
SRCS += main_process.cpp
SRCS += call.cpp
OBJS = $(SRCS:.cpp=.o)
INCDIR = -I.
LIBDIR = 
LIBS =
$(TARGET): $(OBJS)
	$(CC) -o $@ $^ $(LIBDIR) $(LIBS)

$(OBJS): $(SRCS)
	$(CC) $(CFLAGS) $(INCDIR) -c $(SRCS)

all: clean $(OBJS) $(TARGET)

clean:
	-rm -f $(OBJS) $(TARGET) *.d