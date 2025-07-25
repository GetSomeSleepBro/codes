/**
 * Demonstrates multiple inheritance in Java using interfaces, as Java does not
 * support extending multiple classes.  Two interfaces (Singer and Dancer) are
 * implemented by a single class (Performer) and a polymorphic routine is
 * showcased.
 */
interface Singer {
    void sing();
}

interface Dancer {
    void dance();
}

class Performer implements Singer, Dancer {
    private final String name;

    Performer(String name) {
        this.name = name;
    }

    @Override
    public void sing() {
        System.out.println(name + " is singing 🎤");
    }

    @Override
    public void dance() {
        System.out.println(name + " is dancing 💃");
    }
}

public class MultipleInheritanceDemo {
    public static void main(String[] args) {
        Performer p = new Performer("Alex");
        // Polymorphic calls
        performShow(p);
    }

    private static void performShow(Singer singer) {
        // Argument is typed as Singer, yet also has Dancer behaviour thanks to interfaces
        singer.sing();
        if (singer instanceof Dancer dancer) {
            dancer.dance();
        }
    }
}
