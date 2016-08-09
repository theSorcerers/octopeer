FactoryGirl.define do
  factory :mouse_position_event do
    session
    sequence(:position_x)
    sequence(:position_y)
    sequence(:viewport_x)
    sequence(:viewport_y)
  end
end
