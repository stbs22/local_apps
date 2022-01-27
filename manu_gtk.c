#include <gtk/gtk.h>
#define WINDOW_SIZE 50

static int COUNT = 0;

void welcome(GtkWidget*, gpointer);
void destroy(GtkWidget*, gpointer);

int main(int argc, char* argv[]){
	GtkWidget* window;
	GtkWidget* button;

	gtk_init(&argc, &argv);
	window = gtk_window_new(GTK_WINDOW_TOPLEVEL);

	g_signal_connect(window, "destroy", G_CALLBACK(destroy), NULL);

	gtk_container_set_border_width(GTK_CONTAINER(window), WINDOW_SIZE);

	button = gtk_button_new_with_label("Click Me!");

	g_signal_connect(G_OBJECT(button), "clicked", G_CALLBACK(welcome), "button");

	gtk_container_add(GTK_CONTAINER(window), button);
	gtk_widget_show_all(window);
	gtk_main();

	return 0;
}

void welcome(GtkWidget* widget, gpointer data){
	// printf equivalent in GTK+
	g_print("Hello World!\n");
	g_print("%s Clicked %d times\n", (char*)data, ++COUNT);
}

void destroy(GtkWidget* widget, gpointer data){
	gtk_main_quit();
}
