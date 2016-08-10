class Api::KeystrokeTypesController < ApplicationController
  include Showable
  include Indexable
  include Createable

  private

  def keystroke_type_params
    params.require(:keystroke_type).permit(:name)
  end
end
