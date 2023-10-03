program main

  use read_dcd
  implicit none

  character(len=50) :: dcd_name, exyz_name

  integer :: N, snapshots, snapshot, fnum=302, i, type, sampling
  logical :: uc_present
  real, dimension(:,:), allocatable :: positions
  real(kind=real64), dimension(3, 3) :: uc_vecs
  
  CALL GET_COMMAND_ARGUMENT(1, dcd_name)  
  CALL GET_COMMAND_ARGUMENT(2, exyz_name)
  
  CALL read_dcd_header(TRIM(dcd_name), N, snapshots, uc_present)

  allocate(positions(3, N))

  ! Paraview kept quitting when opening whole file - either can't handle exyz or something else
  
  open(fnum, file=TRIM(exyz_name), status='new')

  type = 1 ! All atoms of same type
  sampling = 100 ! Get snapshot every 100 timesteps
  
  do snapshot=1, snapshots
     call read_dcd_snapshot(TRIM(dcd_name), N, snapshot, uc_present, positions, uc_vecs)
     write(fnum, *) '# Timestep: ', (1-snapshot)*sampling
     write(fnum, '(I15)') N
     write(fnum, *) '%PBC'
     do i = 1, N
        write(fnum, '(I6 F15.5 F15.5 F15.5)') type, positions(1, i), positions(2, i), positions(3, i)
     end do
     write(fnum, *) ''
     write (fnum, '(A7 F15.5 F15.5 F15.5)') 'Vector1', uc_vecs(1, 1), uc_vecs(1, 2), uc_vecs(1, 3)
     write (fnum, '(A7 F15.5 F15.5 F15.5)') 'Vector1', uc_vecs(2, 1), uc_vecs(2, 2), uc_vecs(2, 3)
     write (fnum, '(A7 F15.5 F15.5 F15.5)') 'Vector1', uc_vecs(3, 1), uc_vecs(3, 2), uc_vecs(3, 3)
     write (fnum, '(A7 F15.5 F15.5 F15.5)') 'Offset ', 0.0, 0.0, 0.0
     write(fnum, *) '#'
  end do

  deallocate(positions)
  close(fnum)
  
end program main
