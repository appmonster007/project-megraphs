#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

// Reads a line into buffer
// Discards newline chrachter at the end
int freadline(char *buffer, FILE *fp) {
    char c;
    char *putter = buffer;
    int count = 0;

    // Check whether file is exhausted
    // In which case the we return -1
    if (feof(fp)) {
        return -1;
    }

    // Copy until we reach a newline charachter
    while ((c = fgetc(fp)) != EOF && c != '\n') {
        *putter = c;
        putter += 1;
        count += 1;
    }

    // Terminate the buffer
    *putter = '\0';
    
    // return the number of charachters stored
    return count;
}

struct Edge {
    uint32_t from;
    uint32_t to;
};

struct Graph {
    enum {DIRECTED, UNDIRECTED} type;
    uint32_t nodes;
    uint32_t number_of_edges;
    struct Edge *edges;
};

void destroy(struct Graph g) {
    g.nodes = 0;
    g.number_of_edges = 0;
    free(g.edges);
}

size_t get_size(struct Graph g) {
    return (sizeof(enum {T1, T2}) + sizeof(uint32_t) + sizeof(uint32_t) + sizeof(struct Edge) * g.number_of_edges);
}

int degree(struct Graph g, uint32_t node) {
    int degree = 0;
    int outgoing = 0;
    int incoming = 0;
    for (uint32_t i = 0; i < g.number_of_edges; i++) {
        if (g.edges[i].from == node) {
            outgoing += 1;
        }
        if (g.edges[i].to == node) {
            incoming += 1;
        }
    }
    degree = outgoing + incoming;
    return degree;
}

int degree2(struct Graph g, uint32_t node) {
    int d2 = 0;
    int double_count = 0;

    for (uint32_t i = 0; i < g.number_of_edges; i++) {
        if (g.edges[i].from == node) {
            d2 += degree(g, g.edges[i].to);
            double_count += 1;
        }

        if (g.edges[i].to == node) {
            d2 += degree(g, g.edges[i].from);
            double_count += 1;
        }
    }

    return d2 - double_count;
}

int main(int argc, char *argv[]) {
    char buffer[128] = {0};
    int chars = 0;
    int lines = 0;
    FILE *fp = fopen(argv[1], "r");

    // Skip all comments
    while ((chars = freadline(buffer, fp)) != -1 && buffer[0] == '%') {
        lines++;
    }

    printf("Read %d lines of comments\n", lines);

    uint32_t nodes;
    uint32_t edges;
    uint32_t temp;
    sscanf(buffer, "%d %d %d", &nodes, &temp, &edges);

    printf("Nodes = %d\n", nodes);
    printf("Edges = %d\n", edges);

    struct Graph g = {
        .type = UNDIRECTED,
        .nodes = nodes,
        .edges = malloc(sizeof(struct Edge) * edges),
        .number_of_edges = edges
    };

    int ec = 0;
    while ((chars = freadline(buffer, fp)) != -1 && buffer[0] != '%') {
        uint32_t from, to;
        sscanf(buffer, "%d %d", &from, &to);
        g.edges[ec].from = from;
        g.edges[ec].to = to;
        ec += 1;
    }

    int *degrees2 = malloc(sizeof(int) * g.nodes);
    
    for (uint32_t i = 1; i < g.nodes; i++) {
        degrees2[i] = degree2(g, i);
        printf("2nd order degree of %d is: %d\n", i, degrees2[i]);
    }

    printf("Size of graph structure = %zu bytes\n", get_size(g));
    destroy(g);
}

