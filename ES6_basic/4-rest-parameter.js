export default function returnHowManyArguments(...RestArg) {
    let total = 0;
    for (const arg of RestArg) {
        total += 1;
    }
    return total;
}