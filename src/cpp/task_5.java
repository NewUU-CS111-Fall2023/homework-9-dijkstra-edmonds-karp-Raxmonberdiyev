/*
 * Author:
 * Date:
 * Name:
 */

import java.util.*;

class Main {
    static class Flight {
        int to;
        int price;

        Flight(int to, int price) {
            this.to = to;
            this.price = price;
        }
    }

    static class City {
        int city;
        int price;
        int stops;

        City(int city, int price, int stops) {
            this.city = city;
            this.price = price;
            this.stops = stops;
        }
    }

    public static int findCheapestPrice(int[][] flights, int src, int dst, int K) {
        Map<Integer, List<Flight>> graph = new HashMap<>();
        for (int[] flight : flights) {
            graph.putIfAbsent(flight[0], new ArrayList<>());
            graph.get(flight[0]).add(new Flight(flight[1], flight[2]));
        }

        PriorityQueue<City> pq = new PriorityQueue<>(Comparator.comparingInt(a -> a.price));
        pq.add(new City(src, 0, 0));

        while (!pq.isEmpty()) {
            City top = pq.poll();

            if (top.city == dst) {
                return top.price;
            }

            if (top.stops <= K) {
                List<Flight> flightsFromHere = graph.get(top.city);
                if (flightsFromHere != null) {
                    for (Flight flight : flightsFromHere) {
                        pq.add(new City(flight.to, top.price + flight.price, top.stops + 1));
                    }
                }
            }
        }

        return -1;
    }

    public static void main(String[] args) {
        // Your code here
    }
}

;