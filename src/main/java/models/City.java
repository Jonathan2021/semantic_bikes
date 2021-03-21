package models;

import java.util.ArrayList;
import java.util.List;

public class City {
    private String name;
    private String country;
    private List<Station> bikeStations = new ArrayList<Station>();

    public void addStation(Station bikeStation) {
        this.bikeStations.add(bikeStation);
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getCountry() {
        return country;
    }

    public void setCountry(String country) {
        this.country = country;
    }

    public List<Station> getStations() {
        return bikeStations;
    }

    public void setStations(List<Station> bikeStations) {
        this.bikeStations = bikeStations;
    }
}

