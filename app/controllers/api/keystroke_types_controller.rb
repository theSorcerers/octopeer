class Api::KeystrokeTypesController < ApplicationController
  include Showable
  include Indexable
  include Createable

  private

  def parameters
    params.require(:keystroke_type).permit(:name)
  end
end
