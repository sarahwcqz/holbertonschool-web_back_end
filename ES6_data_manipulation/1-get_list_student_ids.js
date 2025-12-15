export default function getListStudents(list){
    if (!Array.isArray(list)) {
        return [];
    }

    return list.map(student => student.id);
}